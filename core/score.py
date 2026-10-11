#!/usr/bin/env python3
"""ICE 점수 계산과 S~D 등급 부여.

사용법:
    python score.py input.json            # 파일에서 읽기
    cat input.json | python score.py -    # 표준입력에서 읽기

입력(JSON):
{
  "jobs": [
    {"id": "A", "title": "...", "company": "...",
     "impact": 8, "confidence": 6, "ease": 7, "reason": "근거 한 줄",
     "role": "PM", "track": "target"}          # track: target(목표 직군) | adjacent(현재 직무 연장)
  ],
  "roles": ["서비스 기획", "PM"],                          # 선택, 확정된 목표 직군 (직군별 최소 개수 점검용)
  "adjacent_roles": ["그로스 마케터"],                      # 선택, 현재 직무와 같은 계열의 직군. 이 직군 공고가 track=target이면 경고
  "max_adjacent": 2,                                       # 선택, 현재 직무 연장 공고 최대 개수 (기본 2)
  "min_per_role": 2,                                       # 선택, 직군별 최소 공고 수 (기본 2)
  "weights": {"impact": 1, "confidence": 1, "ease": 1},   # 선택, 기본은 동일 가중치
  "hold_below": 60                                         # 선택, 기본 60 (테스트 후 조정 가능)
}

출력(JSON): 점수 내림차순 정렬된 공고 목록과 등급, 경고 메시지.
점수 = 가중 평균(1~10) x 10 → 10~100점.
동점 처리: Confidence → Impact → Ease → 입력 순서.
"""

import json
import sys

# 등급 배분 (S 1, A 2, B 3, C 2, D 2). 공고가 10개 미만이면 앞에서부터 사용한다.
GRADE_SLOTS = ["S"] + ["A"] * 2 + ["B"] * 3 + ["C"] * 2 + ["D"] * 2

DEFAULT_WEIGHTS = {"impact": 1.0, "confidence": 1.0, "ease": 1.0}
DEFAULT_HOLD_BELOW = 60
DEFAULT_MAX_ADJACENT = 2
DEFAULT_MIN_PER_ROLE = 2
ADJACENT_IMPACT_CAP = 5   # 현재 직무 연장 공고의 Impact 상한 (ice-rubric.md)


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
    hold_below = data.get("hold_below", DEFAULT_HOLD_BELOW)

    errors = []
    if not jobs:
        errors.append("jobs가 비어 있어요")
    for i, job in enumerate(jobs):
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
    if len(scored) != len(GRADE_SLOTS):
        warnings.append(
            f"공고가 {len(scored)}개예요 (기본 {len(GRADE_SLOTS)}개). 등급은 위에서부터 배분했어요."
        )

    max_adjacent = data.get("max_adjacent", DEFAULT_MAX_ADJACENT)
    min_per_role = data.get("min_per_role", DEFAULT_MIN_PER_ROLE)
    adjacent = [j for j in scored if j.get("track") == "adjacent"]
    if len(adjacent) > max_adjacent:
        warnings.append(
            f"현재 직무 연장(adjacent) 공고가 {len(adjacent)}개예요 (최대 {max_adjacent}개). 후보를 조정해 주세요."
        )
    # 현재 직무 계열인데 목표(target)로 표시된 공고를 잡는다 (사용자가 골랐어도 연장선이다)
    adjacent_roles = set(data.get("adjacent_roles", []))
    for job in scored:
        if job.get("role") in adjacent_roles and job.get("track") != "adjacent":
            warnings.append(
                f"{job.get('id', '?')}: 직군 '{job.get('role')}'은 현재 직무 계열이에요. track을 adjacent로 바꿔 주세요."
            )
    for job in adjacent:
        if job["impact"] > ADJACENT_IMPACT_CAP:
            warnings.append(
                f"{job.get('id', '?')}: 현재 직무 연장 공고는 Impact {ADJACENT_IMPACT_CAP} 이하여야 해요 (값: {job['impact']})."
            )
    for role in data.get("roles", []):
        count = sum(1 for j in scored if j.get("role") == role)
        if count < min_per_role:
            warnings.append(
                f"직군 '{role}' 공고가 {count}개예요 (최소 {min_per_role}개). 부족하면 사유를 리포트에 적어주세요."
            )

    for rank, job in enumerate(scored, start=1):
        job["rank"] = rank
        job["grade"] = GRADE_SLOTS[rank - 1] if rank <= len(GRADE_SLOTS) else "D"
        job["hold"] = job["score"] < hold_below
        del job["_order"]

    top_adjacent = [j.get("id", "?") for j in scored if j.get("track") == "adjacent" and j["grade"] in ("S", "A")]
    if top_adjacent:
        warnings.append(
            f"안전 선택지({', '.join(top_adjacent)})가 S/A 등급이에요. 목표 직군 공고의 Confidence·Ease를 다시 점검해 주세요."
        )

    return {
        "ok": True,
        "hold_below": hold_below,
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
