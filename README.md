# get-you-design-hired · 디자인 커리어

> **English summary** — A personal job-search agent for designers that gets to know you from your AI chat history. Give an AI assistant (Claude or any AI that can browse) this repo link with your chats, and optionally your resume, cover letter and portfolio. It asks three short questions, shows what kind of person your conversations point to (with evidence), finds 10 Korean job postings for four design roles (product, content, BX, brand), ranks them 1–10 with ICE scoring and a requirement checklist, and writes a DOCX report with strengths, weaknesses, blind spots and a 3-day plan. Then it consults on your top 1–3 companies one at a time: a 3Q story (direction, metacognition, consistency), requirement gaps, portfolio order, document fixes, likely interview questions, and one dated action. Save the career file it gives you; next time it starts by asking how that action went. No server, nothing collected. Work in progress. MIT licensed.

AI와 나눈 대화 기록으로 나를 알아가는 **디자이너를 위한 나만의 취업 도우미**예요. 대화에서 보이는 내 모습과 어울리는 직군을 짚어주고, 나에게 맞는 채용 공고 10개의 순서와 리포트(DOCX)를 만들어요. 그다음 1~3위 회사를 하나씩 골라 서류·포트폴리오·면접까지 같이 준비하고, 오늘 할 일을 날짜까지 정해요. 저장해 둔 커리어 파일을 다시 올리면 처음부터 묻지 않고, 지난번에 하기로 한 일부터 이어서 상담해요.

대상 직군: **프로덕트 디자이너, 콘텐츠 디자이너, BX 디자이너, 브랜드 디자이너**

> 🚧 제작 중이에요. 지금은 **한국 공고만** 지원해요.

## 바로 쓰기

Claude처럼 웹을 읽을 수 있는 AI의 **새 대화**에서 파일을 첨부하고 이렇게 보내요.

```
https://github.com/iljunlee-kai/get-you-hired 의 START.md를 읽고 그대로 진행해줘.
첨부한 건 내 AI 대화 기록이야. (이력서·자소서도 있으면 같이 첨부)
```

에이전트가 이 레포를 직접 읽고 진행해요. 따로 설치하거나 설정할 것은 없어요. ChatGPT에서 커스텀 GPT로 쓰고 싶다면 [gpt/README.md](gpt/README.md)를 보세요.

## 준비물

| 자료 | 필요 여부 | 쓰이는 곳 |
|---|---|---|
| AI와 나눈 대화 기록 (MD 파일) | 필수 | 나를 알아가는 근거, 맹점 분석 |
| 이력서·자기소개서 (PDF, Word, 텍스트) | 선택, 있으면 정확해져요 | 경력·학력 확인, 요건 대조, 서류 점검 |
| 포트폴리오 (PDF) | 지원 전략 단계에서 | 회사별로 앞에 둘 사례와 고칠 점 |

포트폴리오가 30MB를 넘거나 페이지가 많으면, 프로젝트 카드(프로젝트마다 이름·내 역할·기여도·성과 한 줄)와 대표 사례의 핵심 페이지 3~5장만 올려도 돼요.

## 이렇게 진행돼요

1. **자료 읽기와 질문 3개.** 대화 기록(과 서류)을 끝까지 읽은 뒤, 원하는 직군·연봉·지역·조건 / 학력 / 잘하는 것·어려운 것을 하나씩 물어요. 이력서에 있는 학력은 확인만 해요. 답이 대화나 서류와 다르면 어느 쪽이 맞는지 한 번 확인해요.
2. **공고 10개와 순위.** 직군 4개의 실제 공고를 찾아 마감·모집 상태를 페이지에서 읽은 값만 써요. 공고의 요건을 항목별로 내 경험과 대조해 점수를 매기고 1~10위를 정해요. 1~3위에는 모집 중이 확인되고 요건을 읽은 공고만 들어가요.
3. **리포트 (DOCX).** 장점·단점·맹점("대화에서 보이는 당신은 ~한 사람이에요"), 서류 점검, 공고 표, 1~3위 요건 매칭표, 3일 투두가 들어가요.
4. **지원 전략 컨설팅.** 1~3위 중 한 회사를 골라요.
   - **3Q로 내 이야기 정리** (처음 한 번): 방향, 강점과 약점(메타인지), 왜 이 분야인지(일관성). 에이전트가 근거를 붙인 초안을 보여주고, 나는 고치기만 해요.
   - **회사별 준비**: 확인이 필요한 요건 질문, 부족한 요건의 대응 방법, 포트폴리오 사례 순서, 서류 문장 수정, 예상 면접 질문, 지원 경로.
   - **오늘 할 일**: 마감까지 일정과, 오늘 할 30분짜리 행동 하나를 언제 할지 정해요.
5. **커리어 파일.** 마지막에 나오는 블록을 `커리어파일.md`로 저장해 두세요. 다음에 올리면 이미 확인한 내용은 다시 묻지 않고, 지난번에 약속한 행동이 어떻게 됐는지부터 물어요.
6. **지원 결과.** 다음 상담에서 지원 결과(통과·탈락·연락 없음)를 알려 주면 기록해 두고, 서로 다른 공고에서 같은 이유가 2번 이상 반복될 때만 다음 추천과 준비 방법에 반영할지 물어요. 탈락 한 번으로 방향을 바꾸지 않아요.

## 알아 둘 점

- **순위는 합격 가능성이 아니라 먼저 볼 순서**예요. 점수도 함께 보여줘요.
- 채용 사이트마다 AI가 읽을 수 있는 정도가 달라요. 요건을 못 읽은 공고는 표시해 두고, 관심 있는 공고의 JD를 붙여 주면 다시 맞춰 봐요.
- 포트폴리오의 **시각적 완성도는 평가하지 않아요.** 공고와 맞는지, 구성과 내 역할이 잘 보이는지를 봐요. 이미지로만 된 PDF는 읽기 어려울 수 있어서, 에이전트가 실제로 본 페이지를 밝혀요.
- 서류 문장을 대신 지어내지 않아요. 제안은 내가 말했거나 서류에 있는 사실 안에서만 해요.

## 개인정보

- 이 레포는 서버가 없고 아무것도 수집하지 않아요. 올린 자료는 지금 쓰는 AI 서비스의 채팅 안에서만 분석되고, 보관은 그 서비스의 정책을 따라요.
- 이름, 연락처, 이메일, 주소, 생년월일은 리포트와 커리어 파일에 옮기지 않아요. 그래도 올리기 전에 지우는 게 좋아요.
- 커리어 파일에는 서류 내용이 저장되지 않아요. 다음에 지원 전략을 이어 할 때는 서류를 다시 올려 주세요.

## 폴더 구조

```
├── README.md
├── START.md                  에이전트 시작 파일 (꼭 지킬 것, 흐름, 읽을 파일 목록)
├── core/
│   ├── principles.md         원칙·정지 지점·금지
│   ├── flow-intake.md        단계 1: 자료 읽기·질문·프로필
│   ├── flow-search-score.md  단계 2: 공고 검색·요건 체크리스트·순위
│   ├── flow-report.md        단계 3: 리포트
│   ├── flow-resume.md        단계 4: 커리어 파일·이어가기
│   ├── flow-strategy.md      단계 5: 지원 전략 컨설팅 (3Q, 회사별 준비, 행동)
│   ├── flow-feedback.md      단계 6: 지원 결과 기록과 반복 패턴 반영
│   ├── roles.md              직군 4개 정의·검색어·판정 기준
│   ├── ice-rubric.md         ICE 기준과 요건 체크리스트
│   ├── score.py              점수·순위 계산
│   ├── career-file.md        커리어 파일 형식
│   └── sample-input.json     score.py 예시 입력
├── i18n/
│   ├── ko/                   한국어 질문·문구·리포트·지원 전략 질문
│   └── en/                   영어 (준비 중)
├── sources.yml               공고 사이트 목록과 접근 테스트 기록
├── gpt/                      커스텀 GPT로 쓸 때의 설정과 확인 순서
├── examples/                 테스트용 가상 자료 (대화, 이력서, 자소서, 포트폴리오 PDF, 커리어 파일)
└── docs/                     공고 사이트 접근 테스트 방법
```

## 개발자용

- 점수 계산은 직접 돌려볼 수 있어요.
  ```bash
  python core/score.py core/sample-input.json
  ```
- 원본은 이 레포 하나예요. 에이전트가 `main` 브랜치를 직접 읽으니, **push하는 순간 사용 중인 대화에도 반영돼요.** 고치기 전후로 `examples/`의 가상 자료로 확인하세요.
- 모든 지침 파일의 마지막 줄은 끝 표시(`<!-- END: 경로 -->`)예요. 에이전트가 파일을 끝까지 읽었는지 확인하는 데 쓰니 지우지 마세요.
- 테스트할 때는 AI의 메모리나 과거 대화 참조를 끄고 하세요. 이전 버전 규칙이 기억으로 섞일 수 있어요. 확인 순서는 [gpt/README.md](gpt/README.md)의 "저장 후 확인"을 그대로 쓰면 돼요.

## 라이선스

MIT. [LICENSE](LICENSE)를 보세요.
