#!/usr/bin/env python3
"""ICE 점수 계산과 1~N위 순위 부여.

사용법:
    python score.py input.json            # 파일에서 읽기
    cat input.json | python score.py -    # 표준입력에서 읽기

입력(JSON):
{
  "jobs": [
    {"id": "A", "title": "...", "company": "...",
     "impact": 8, "confidence": 6, "ease": 7, "reason": "근거 한 줄",
     "role": "프로덕트 디자이너",                 # search_roles 항목과 같은 문자열
     "status": "open", "deadline": "2026-10-20",  # status: open(모집 중 확인) | closed(마감) | unknown(못 읽음)
     "requirements_read": true,                  # 주요업무·자격요건을 상세 페이지에서 읽었는지 (생략하면 true)
     "years_required": 3,                        # 선택, 공고의 최소 요구 연차
     "requirements": [                           # 선택, 요건 체크리스트. 있으면 Confidence를 여기서 계산한다
       {"text": "Figma 활용", "type": "must", "status": "met", "evidence": "이력서: Figma 화면 32개"}
       # type: must(자격요건) | pref(우대사항)
       # status: met(충족) | partial(부분) | unmet(미충족) | unknown(확인 불가: 사용자에게 물어볼 것)
     ]}
                                                   # deadline: YYYY-MM-DD, 상시채용이면 "상시", 못 읽었으면 생략
  ],
  "today": "2026-10-25",
  "experience_years": 3,                                   # 선택, 프로필의 연차. years_required와 비교한다                                   # 선택, 오늘 날짜. 있으면 마감일이 지난 공고를 경고한다
  "roles": ["프로덕트 디자이너", "BX 디자이너"],           # 선택, 검색 직군(search_roles). 직군별 최소 개수 점검용
  "min_per_role": 2,                                       # 선택, 직군별 최소 공고 수 (기본 2)
  "top_n": 3,                                              # 선택, 모집 상태를 확인해야 하는 상위 순위 (기본 3)
  "weights": {"impact": 1, "confidence": 1, "ease": 1},   # 선택, 기본은 동일 가중치
  "low_score_below": 60                                    # 선택, 1위 점수가 이보다 낮으면 top_score_low=true (기본 60)
}

출력(JSON): 점수 내림차순으로 정렬하고 rank(1부터)를 붙인 공고 목록, top_score_low, 경고 메시지.
1~top_n위에는 모집 중이 확인되고 요건을 읽은 공고(top_eligible)만 둔다. 아닌 공고는 점수가 높아도 그 아래로 내린다.
점수 = 가중 평균(1~10) x 10 → 10~100점.
동점 처리: Confidence → Impact → Ease → 입력 순서.
등급 문자(S~D)와 "추천 보류"는 쓰지 않는다 (2026-10-25, D31).

Confidence (D34): 공고에 requirements가 있으면 입력한 confidence 대신 체크리스트로 계산한다.
  항목 점수: met 1, partial 0.5, unmet 0, unknown 0 (unknown은 확인 질문으로 따로 돌려준다).
  비율 = 필수 평균 x 0.75 + 우대 평균 x 0.25 (우대가 없으면 필수 평균, 필수가 없으면 우대 평균).
  Confidence = round(1 + 9 x 비율), 1~10.
  years_required - experience_years >= 3 이면 Confidence 3 이하.
  출력: confidence_source(checklist|judged), checklist(must/pref 충족 수), gaps(unmet·partial), unknowns.
"""

import json
import sys
from datetime import date

DEFAULT_WEIGHTS = {"impact": 1.0, "confidence": 1.0, "ease": 1.0}
DEFAULT_LOW_SCORE_BELOW = 60
DEFAULT_MIN_PER_ROLE = 2
DEFAULT_TOP_N = 3
EXPECTED_COUNT = 10
ITEM_POINTS = {"met": 1.0, "partial": 0.5, "unmet": 0.0, "unknown": 0.0}
EXPERIENCE_GAP_YEARS = 3
EXPERIENCE_GAP_CAP = 3


def apply_checklist(job, experience_years, errors, index):
    """requirements가 있으면 Confidence를 계산해 job에 넣는다."""
    reqs = job.get("requirements")
    if reqs:
        groups = {"must": [], "pref": []}
        gaps, unknowns = [], []
        for k, item in enumerate(reqs):
            kind, status = item.get("type"), item.get("status")
            if kind not in groups or status not in ITEM_POINTS:
                errors.append(f"jobs[{index}].requirements[{k}]: type은 must/pref, status는 met/partial/unmet/unknown이어야 해요")
                continue
            groups[kind].append(ITEM_POINTS[status])
            if status in ("unmet", "partial"):
                gaps.append({"text": item.get("text", ""), "type": kind, "status": status})
            elif status == "unknown":
                unknowns.append({"text": item.get("text", ""), "type": kind})
        must = sum(groups["must"]) / len(groups["must"]) if groups["must"] else None
        pref = sum(groups["pref"]) / len(groups["pref"]) if groups["pref"] else None
        if must is not None and pref is not None:
            ratio = must * 0.75 + pref * 0.25
        else:
            ratio = must if must is not None else (pref if pref is not None else 0.0)
        job["confidence"] = max(1, min(10, round(1 + 9 * ratio)))
        job["confidence_source"] = "checklist"
        job["checklist"] = {
            "must_met": sum(1 for p in groups["must"] if p == 1.0), "must_total": len(groups["must"]),
            "pref_met": sum(1 for p in groups["pref"] if p == 1.0), "pref_total": len(groups["pref"]),
        }
        job["gaps"], job["unknowns"] = gaps, unknowns
        job.setdefault("requirements_read", True)
    else:
        job["confidence_source"] = "judged"
    yr = job.get("years_required")
    if (isinstance(yr, (int, float)) and isinstance(experience_years, (int, float))
            and yr - experience_years >= EXPERIENCE_GAP_YEARS
            and isinstance(job.get("confidence"), (int, float))
            and job["confidence"] > EXPERIENCE_GAP_CAP):
        job["confidence"] = EXPERIENCE_GAP_CAP
        job["experience_capped"] = True


def validate(job, index, errors):
    for key in ("impact", "confidence", "ease"):
        value = job.get(key)
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            errors.append(f"jobs[{index}].{key}: 숫자여야 해요")
        elif not 1 <= value <= 10:
            errors.append(f"jobs[{index}].{key}: 1~10 범위여야 해요 (값: {value})")


def compute(data):
    jobs = data.get("jobs", [])
    weights = {**DEFAULT_WEIGHTS, **data.get("weights", {})}
    low_score_below = data.get("low_score_below", DEFAULT_LOW_SCORE_BELOW)
    top_n = data.get("top_n", DEFAULT_TOP_N)

    errors = []
    if not jobs:
        errors.append("jobs가 비어 있어요")
    experience_years = data.get("experience_years")
    for i, job in enumerate(jobs):
        apply_checklist(job, experience_years, errors, i)
        validate(job, i, errors)
    total_weight = sum(weights.values())
    if total_weight <= 0:
        errors.append("weights 합이 0보다 커야 해요")
    if errors:
        return {"ok": False, "errors": errors}

    scored = []
    for order, job in enumerate(jobs):
        weighted = (
            job["impact"] * weights["impact"]
            + job["confidence"] * weights["confidence"]
            + job["ease"] * weights["ease"]
        ) / total_weight
        scored.append({**job, "score": round(weighted * 10, 1), "_order": order})

    scored.sort(
        key=lambda j: (-j["score"], -j["confidence"], -j["impact"], -j["ease"], j["_order"])
    )

    warnings = []
    today = None
    if data.get("today"):
        try:
            today = date.fromisoformat(data["today"])
        except ValueError:
            warnings.append(f"today '{data['today']}'를 YYYY-MM-DD로 읽지 못했어요. 마감일 비교를 건너뛰었어요.")

    for job in scored:
        jid = job.get("id", "?")
        status = job.get("status", "unknown")
        deadline = job.get("deadline")
        expired = status == "closed"
        if today and isinstance(deadline, str) and deadline not in ("상시", ""):
            try:
                if date.fromisoformat(deadline) < today:
                    expired = True
            except ValueError:
                warnings.append(f"{jid}: deadline '{deadline}'를 YYYY-MM-DD로 읽지 못했어요.")
        if expired:
            warnings.append(f"{jid}: 마감된 공고예요. 후보에서 빼고 다른 공고로 바꿔 다시 실행해 주세요.")
        reasons = []
        if expired:
            reasons.append("마감")
        elif status != "open":
            reasons.append("모집 상태 미확인")
        if job.get("requirements_read", True) is False:
            reasons.append("요건 미확인")
        job["top_eligible"] = not reasons
        job["_reasons"] = reasons

    # 1~top_n위: 자격 있는 공고를 점수 순으로 채우고, 나머지는 점수 순으로 그 아래에 둔다
    top, rest = [], []
    for job in scored:
        (top if job["top_eligible"] and len(top) < top_n else rest).append(job)
    by_score_rank = {id(j): i for i, j in enumerate(scored, start=1)}
    scored = top + rest
    for rank, job in enumerate(scored, start=1):
        job["rank"] = rank
        if job["_reasons"] and by_score_rank[id(job)] <= top_n:
            warnings.append(
                f"{job.get('id', '?')}: 점수로는 {by_score_rank[id(job)]}위지만 {', '.join(job['_reasons'])}이라 "
                f"{top_n}위 밖({rank}위)으로 내렸어요. 상세 페이지나 JD 원문을 확인하면 다시 올릴 수 있어요."
            )
        del job["_order"], job["_reasons"]
    if len(top) < min(top_n, len(scored)):
        warnings.append(f"1~{top_n}위에 둘 수 있는 공고(모집 중 확인 + 요건 확인)가 {len(top)}개뿐이에요. 리포트에 밝혀 주세요.")

    if len(scored) != EXPECTED_COUNT:
        warnings.append(f"공고가 {len(scored)}개예요 (기본 {EXPECTED_COUNT}개). 개수를 리포트에 밝혀 주세요.")

    min_per_role = data.get("min_per_role", DEFAULT_MIN_PER_ROLE)
    for role in data.get("roles", []):
        count = sum(1 for j in scored if j.get("role") == role)
        if count < min_per_role:
            warnings.append(
                f"직군 '{role}' 공고가 {count}개예요 (최소 {min_per_role}개). 부족하면 사유를 리포트에 적어주세요."
            )

    top_score_low = bool(scored) and scored[0]["score"] < low_score_below

    return {
        "ok": True,
        "low_score_below": low_score_below,
        "top_score_low": top_score_low,
        "weights": weights,
        "warnings": warnings,
        "jobs": scored,
    }


def main():
    if len(sys.argv) != 2:
        print("사용법: python score.py <input.json | ->", file=sys.stderr)
        sys.exit(2)
    source = sys.argv[1]
    try:
        raw = sys.stdin.read() if source == "-" else open(source, encoding="utf-8").read()
        data = json.loads(raw)
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"ok": False, "errors": [str(exc)]}, ensure_ascii=False))
        sys.exit(1)

    result = compute(data)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if result["ok"] else 1)


if __name__ == "__main__":
    main()

# END: core/score.py
