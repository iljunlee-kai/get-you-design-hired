# 커리어 파일 형식 (career-file.md)

규칙 버전: v0.17

세션이 바뀌어도 상담을 이어가기 위해 사용자가 들고 다니는 파일이다. 도구는 이 파일을 저장하지 않는다. 마지막에 출력하면 사용자가 `.md`로 저장하고, 다음에 올린다. 쓸수록 도구가 사용자를 더 잘 아는 상태로 시작하게 하는 것이 목적이다.

## 원칙

- 사용자가 말했거나 도구가 근거와 함께 만든 내용만 넣는다. 지어서 채우지 않는다. 모르면 비운다.
- **확인됨과 추정을 구분한다.** 사용자가 직접 말하거나 맞다고 한 값만 `confirmed`에 넣는다. 도구가 대화에서 읽어낸 값은 추정이고, 사용자가 맞다고 하기 전에는 확인됨으로 올리지 않는다.
- 연락처, 주소, 주민번호 등 개인 식별 정보는 넣지 않는다.
- 사람이 열어서 읽고 고칠 수 있게 짧게 쓴다. 한 칸 한 줄을 지향한다.
- `version`이 다르면 읽을 수 있는 칸만 읽고 나머지는 사용자에게 알린다. `version: 1` 파일은 `confirmed`, `portrait`, `portfolio`가 없는 것으로 읽는다(없는 칸은 비어 있다고 본다).

## 형식

````
```career-file
version: 2
updated: 2026-10-15
language: ko

profile:
  roles: [디자이너]                 # 사용자가 말한 그대로
  search_roles: [프로덕트 디자이너, 콘텐츠 디자이너]   # 실제 검색 직군 (roles.md 4개 중). 해석했으면 확인 후 confirmed에 넣는다
  current_role: 브랜드 디자이너
  experience_years: 3년             # 사용자가 말했거나 이력서에서 계산한 연차. 없으면 비운다
  career_summary: [브랜드 디자이너 3년 8개월 (광고 에이전시)]   # 이력서 기준 한 줄씩. 회사명·연락처 등 식별 정보는 넣지 않는다
  documents: [이력서, 자기소개서]    # 받은 서류 종류만. 내용은 넣지 않는다 (다음 세션에 다시 올려야 함)
  salary: 4500만원 이상
  regions: [서울]
  dealbreakers: [재택 불가]
  interview_checks: [야근 빈도, 팀 문화]
  education: 4년제 시각디자인
  portfolio: 준비중                # 있음 / 준비중 / 없음, 사용자가 말한 대로
  strengths: [비주얼 감각]          # 사용자가 말한 그대로
  weaknesses: [발표]               # 사용자가 말한 그대로
  confirmed: [roles, salary, regions, dealbreakers, education, strengths, weaknesses]   # 사용자가 직접 말했거나 맞다고 한 칸. 이 칸은 다시 묻지 않는다

portrait:                          # "대화에서 보이는 나". 도구의 해석이라 기본은 추정
  - id: T1
    label: 문장과 정보 구조를 먼저 다듬는 사람
    evidence: [대화 3, 대화 5, 대화 6]
    tag: 대화 패턴                  # 대화 패턴 / 대화 속 본인 발언 / 추정
    status: 추정                    # 추정 / 확인됨 / 수정됨 / 기각
    user_note: ""                  # 사용자가 맞다/아니라고 한 말, 고친 표현

story:                             # 3Q 결과 (지원 전략 단계). 사용자가 확정한 문장 그대로
  direction: {text: "", evidence: [], status: 초안}       # 초안 / 확인됨
  metacognition: {text: "", evidence: [], status: 초안}
  consistency: {text: "", evidence: [], status: 초안}

direction:
  chosen: ""                       # 사용자가 정했을 때만 채운다
  hypotheses:
    - id: H1
      text: 비주얼보다 콘텐츠·구조 쪽에 끌린다
      evidence: [대화 3, 대화 5]     # 대화 번호
      tag: 대화 패턴                 # 본인 답변 / 대화 패턴 / 대화 속 본인 발언 / 추정
      status: 가설                   # 가설 / 검증중 / 채택 / 기각
      next_check: 콘텐츠 디자이너 공고 3개 읽고 끌리는지 적어 보기
      result: ""                    # 해 본 결과, 사용자가 말한 대로

postings:
  - id: P1
    company: 회사명
    position: 포지션
    link: https://...
    rank: 1                         # 이번 후보 중 순위 (1~10)
    role: 프로덕트 디자이너
    jd_source: 공고 페이지       # 공고 페이지 / 사용자가 붙여넣음 / 회사 채용 페이지. 1~3위만 아래 칸을 채운다
    years_required: 3
    requirements:                  # 요건 체크리스트 (ice-rubric.md). 근거는 짧게
      - {text: Figma 활용, type: must, status: met, evidence: "이력서"}
      - {text: 사용자 리서치 경험, type: must, status: partial, evidence: "대화 7"}
      - {text: 디자인 시스템 경험, type: pref, status: unknown}
    strategy:                      # 지원 전략을 한 공고만 (flow-strategy.md §15)
      positioning: ""              # 한 줄 포지셔닝
      portfolio_order: []          # 앞에 둘 사례 순서
      doc_fixes: []                # 서류 문장 수정 (원문 → 제안) 요약
      interview_questions: []      # 예상 질문 3개
      route: ""                    # 지원 방법, 추천 경로
      updated: ""
    status: 관심                    # 관심 / 지원 / 서류통과 / 면접 / 탈락 / 합격 / 연락 없음 / 지원 안 함 / 보류
    applied: ""                    # 지원한 날 (YYYY-MM-DD)
    outcomes:                      # 단계별 결과 (flow-feedback.md §16). 사용자가 말한 것만
      - {stage: 서류, date: 2026-11-05, result: 탈락, submitted: "포트폴리오 03→02→01, 서류 수정 반영", reason: "모름", reason_source: 본인 짐작}
    date: 2026-10-15               # 상태가 바뀐 날
    note: ""

next_actions:                      # 다음 세션 첫 질문의 재료
  - id: A1
    text: 마감 확인 후 P1 지원
    due: 이번 주
    status: 미확인                  # 미확인 / 완료 / 못함 / 취소
    result: ""                    # 사용자가 말한 대로

learnings:                         # 지원 결과에서 찾은 패턴 (flow-feedback.md §19)
  - id: L1
    pattern: BX 공고 서류 단계에서 "브랜드 런칭 경험" 요건이 반복해서 걸림
    evidence: [P1, P4]             # 서로 다른 공고
    stage: 서류
    status: 관찰                    # 관찰(1건) / 반복(2건 이상) / 반영(사용자 동의) / 기각
    applied_to: ""                 # 반영한 곳: 검색 / 채점 근거 / 전략 / 가설

history:
  - 2026-10-15: 첫 리포트, 가설 3개, 공고 10개
```
````

## 칸 설명

| 칸 | 내용 | 갱신 시점 |
|---|---|---|
| `profile` | 확정 프로필 블록과 같다 (`core/flow-intake.md` §4) | 조건이 바뀔 때 |
| `profile.confirmed` | 사용자가 직접 말했거나 맞다고 한 칸의 이름 목록 | 사용자가 답하거나 확인할 때 |
| `portrait` | 대화에서 읽은 "나"의 모습. 근거와 상태 포함 | 리포트 작성 때, 이어가기에서 사용자 반응이 있을 때 |
| `direction.hypotheses` | 리포트의 맹점과 방향 추정을 가설로 옮긴 것 | 이어가기 ①에서 |
| `direction.chosen` | 사용자가 직접 정한 방향 | 사용자가 정했을 때만 |
| `postings` | 추천 공고와 지원 상태. 1~3위는 요건 체크리스트(`requirements`)와 출처(`jd_source`)까지 | 공고를 새로 찾거나 이어가기 ③에서 |
| `next_actions` | 다음에 할 일과 지난 결과 | 세션 시작(지난 행동 확인)과 세션 끝 |
| `story` | 3Q(방향·메타인지·일관성). 모든 회사 전략의 바탕 | 지원 전략 단계에서 사용자가 확정할 때 |
| `postings[].strategy` | 그 공고의 지원 전략 요약 | 지원 전략 단계 끝 |
| `postings[].outcomes` | 단계별 지원 결과와 이유 | 결과를 들었을 때 |
| `learnings` | 결과에서 찾은 반복 패턴 | 결과를 기록할 때마다 |
| `history` | 세션당 한 줄 | 세션 끝 |

## 상태 이동 규칙

- 가설: 가설 → 검증중(사용자가 확인 행동을 시작) → 채택(사용자가 맞다고 함) 또는 기각(사용자가 아니라고 함).
- portrait: 추정 → 확인됨(사용자가 맞다고 함) / 수정됨(사용자가 고쳐 말함, `user_note`에 그 표현을 적고 라벨을 그 표현으로 바꿈) / 기각(사용자가 아니라고 함).
- next_actions: 미확인 → 완료 / 못함 / 취소. `result`에는 사용자가 말한 것만 적는다.
- learnings: 관찰(1건) → 반복(서로 다른 공고 2건 이상) → 반영(사용자 동의) 또는 기각(사용자가 아니라고 함). 반영 전에는 추천·전략을 바꾸지 않는다.
- 모든 상태는 **사용자가 한 말**로만 바꾼다. 도구가 짐작으로 올리지 않는다. 기각된 항목은 같은 근거로 다시 추정하지 않는다.

<!-- END: core/career-file.md -->
