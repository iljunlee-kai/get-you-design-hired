# 커리어 파일 형식 (career-file.md)

세션이 바뀌어도 상담을 이어가기 위해 사용자가 들고 다니는 파일이다. 도구는 이 파일을 저장하지 않는다. 마지막에 출력하면 사용자가 `.md`로 저장하고, 다음에 올린다.

## 원칙

- 사용자가 말했거나 도구가 근거와 함께 만든 내용만 넣는다. 지어서 채우지 않는다. 모르면 비운다.
- 연락처, 주소, 주민번호 등 개인 식별 정보는 넣지 않는다.
- 사람이 열어서 읽고 고칠 수 있게 짧게 쓴다. 한 칸 한 줄을 지향한다.
- `version`이 다르면 읽을 수 있는 칸만 읽고 나머지는 사용자에게 알린다.

## 형식

````
```career-file
version: 1
updated: 2026-10-14
language: ko

profile:
  roles: [그로스 마케터, PM]
  current_role: 온라인 마케터
  salary: 5000만원 이상
  regions: [서울]
  dealbreakers: [재택 불가]
  interview_checks: [야근 빈도, 팀 문화]
  education: 4년제 경영학
  strengths: [데이터 보는 눈]      # 사용자가 말한 그대로
  weaknesses: [발표]              # 사용자가 말한 그대로

direction:
  chosen: ""                       # 사용자가 정했을 때만 채운다
  hypotheses:
    - id: H1
      text: 기획보다 분석에 끌린다
      evidence: [대화 3, 대화 5]     # 대화 번호
      tag: 대화 패턴                 # 본인 답변 / 대화 패턴 / 대화 속 본인 발언 / 추정
      status: 가설                   # 가설 / 검증중 / 채택 / 기각
      next_check: 데이터 분석가 공고 3개 읽고 끌리는지 적어 보기
      result: ""                    # 해 본 결과, 사용자가 말한 대로

postings:
  - id: P1
    company: 회사명
    position: 포지션
    link: https://...
    grade: A                        # S/A/B/C/D, 이번 후보 중 우선순위
    status: 관심                    # 관심 / 지원 / 서류통과 / 면접 / 탈락 / 합격 / 보류
    date: 2026-10-14               # 상태가 바뀐 날
    note: ""

next_actions:
  - 이번 주: 마감 확인 후 P1 지원

history:
  - 2026-10-14: 첫 리포트, 가설 3개, 공고 10개
```
````

## 칸 설명

| 칸 | 내용 | 갱신 시점 |
|---|---|---|
| `profile` | 확정 프로필 블록과 같다 (instructions §4) | 조건이 바뀔 때 |
| `direction.hypotheses` | 리포트의 맹점과 방향 추정을 가설로 옮긴 것 | 이어가기 ①에서 |
| `direction.chosen` | 사용자가 직접 정한 방향 | 사용자가 정했을 때만 |
| `postings` | 추천 공고와 지원 상태 | 공고를 새로 찾거나 이어가기 ③에서 |
| `next_actions` | 다음에 할 일 | 세션 끝 |
| `history` | 세션당 한 줄 | 세션 끝 |

## 가설 상태 이동

가설 → 검증중(사용자가 확인 행동을 시작) → 채택(사용자가 맞다고 함) 또는 기각(사용자가 아니라고 함). 상태는 **사용자가 한 말**로만 바꾼다. 도구가 짐작으로 채택하지 않는다.
