# get-you-design-hired · 디자이너 취업 비서

> **English summary** — A job-search assistant for designers that runs inside ChatGPT or Claude from a single prompt. Attach your AI chat history (and optionally your resume and cover letter), and it asks three short questions, finds 10 open Korean postings for four design roles (product, content, BX, brand), checks each top posting's requirements against your experience, ranks them, and writes a DOCX report. Then it prepares one company at a time with you — your 3Q story, requirement gaps, portfolio order, document fixes, likely interview questions and a dated next step. Save the career file it gives you; next time you only upload that file and it picks up where you left off, including how your applications went. No server, nothing collected. Work in progress. MIT licensed.

**다시 설명하지 않아도 공고부터 서류, 일정, 지원 결과까지 이어서 챙겨 주는 디자이너용 취업 비서**예요.

- **알아서 찾고 대조해요.** 지금 모집 중인 공고 10개를 찾아 마감 공고는 빼고, 1~3위는 요건을 하나씩 내 경력과 맞춰 봐요. 미리 찾아 둔 공고나 꼭 가고 싶은 회사도 같이 체크해요.
- **지원 준비까지 같이 해요.** 회사 하나를 고르면 서류 문장, 포트폴리오 순서, 예상 면접 질문, 마감까지 일정을 정리해요.
- **다음엔 파일 하나로 이어가요.** 커리어 파일만 올리면 이미 말한 건 다시 묻지 않고, 지난번 할 일과 지원 결과부터 이어서 봐요.
- **지어내지 않아요.** 공고 페이지에서 읽은 값만 쓰고, 점수는 코드로 계산하고, 서류 문장은 내가 말한 사실 안에서만 고쳐요.

대상 직군: **프로덕트 디자이너, 콘텐츠 디자이너, BX 디자이너, 브랜드 디자이너**

> 🚧 제작 중이에요. 지금은 **한국 공고만** 지원해요.

## 바로 쓰기

### 1. 준비물

| 자료 | 필요 여부 | 쓰이는 곳 |
|---|---|---|
| AI와 나눈 대화 기록 (`.md` 또는 `.txt`) | 필수 | 다시 묻지 않고 나를 파악하는 재료 |
| 이력서·자기소개서 (PDF, Word, 텍스트) | 선택, 있으면 정확해져요 | 경력·학력 확인, 요건 대조, 서류 점검 |
| 포트폴리오 (PDF) | 지원 전략 단계에서 | 회사별로 앞에 둘 사례와 고칠 점 |

- 대화 기록은 대화를 열어 전체 선택 → 복사 → 메모장에 붙여 `.txt`로 저장하면 돼요. 여러 대화는 한 파일에 이어 붙여도 돼요.
- 연락처·주민번호 같은 개인정보는 지우고 올리는 걸 권해요.
- 포트폴리오가 30MB를 넘으면 핵심 프로젝트 3~5쪽만 따로 저장해 올려도 돼요.

### 2. ChatGPT·Claude 설정

**새 채팅**에서 시작하세요 (맞춤 GPT 말고 일반 채팅). **웹 검색**과 **코드 실행**(점수 계산·리포트 파일 만들기)이 켜져 있어야 해요. 보통은 이미 켜져 있어요.

### 3. 시작 문장 (파일을 첨부하고 그대로 보내기)

처음 시작할 때:
```
https://raw.githubusercontent.com/iljunlee-kai/get-you-design-hired/stable/START.md?t=202610281500 을 열어서 마지막 줄 <!-- END: START.md --> 까지 읽고 그대로 진행해줘.
START.md 안의 파일 주소는 ?v= 꼬리까지 그대로 열어줘.
첨부한 건 내 AI 대화 기록이야. 이력서와 자기소개서도 같이 첨부했어.
```

이어서 할 때 (`커리어파일.md`를 첨부):
```
https://raw.githubusercontent.com/iljunlee-kai/get-you-design-hired/stable/START.md?t=202610281500 을 열어서 마지막 줄 <!-- END: START.md --> 까지 읽고 그대로 진행해줘.
START.md 안의 파일 주소는 ?v= 꼬리까지 그대로 열어줘.
첨부한 건 지난번에 받은 내 커리어 파일이야.
```

`?t=` 뒤 숫자는 지금 날짜·시각으로 바꿔 주세요. AI의 웹 읽기 도구가 예전에 저장해 둔 사본을 주지 않게 하는 장치예요. 첫 답장 첫 줄에 개인정보 안내가 나오면 제대로 시작된 거예요.

## 이렇게 진행돼요

1. **질문 3개.** 원하는 직군·연봉·지역·조건 / 학력과 포트폴리오 상태 / 잘하는 것·어려운 것을 하나씩 물어요. 이력서에 있는 학력은 확인만 해요. 마지막 질문에서 미리 찾아본 공고나 꼭 가고 싶은 회사가 있는지도 물어요.
2. **공고 10개와 순위.** 직군 4개의 실제 공고를 찾아 마감 공고는 빼고, 요건을 내 경험과 대조해 점수를 매겨요. 1~3위에는 모집 중이 확인되고 요건을 읽은 공고만 들어가요.
3. **리포트 (DOCX).** 총평, 장단점·맹점, 서류 점검, 공고 표, 1~3위 요건 매칭표, 먼저 확인할 것이 들어가요.
4. **지원 전략.** 1~3위 중 한 회사를 골라요. 3Q(방향·강점과 약점·왜 이 분야인지) 초안을 한 번에 보여주고 고칠 것만 받아요. 이어서 부족한 요건 대응, 포트폴리오 순서, 서류 문장 수정, 예상 면접 질문, 마감까지 일정과 오늘 할 일을 정해요.
5. **커리어 파일.** 마지막에 나오는 블록을 `커리어파일.md`로 저장해 두세요. 다음에는 이 파일만 올리면 돼요.
6. **지원 결과.** 다음 상담에서 결과(통과·탈락·연락 없음)를 알려 주면 기록해 두고, 서로 다른 공고에서 같은 이유가 2번 이상 반복될 때만 다음 추천과 준비에 반영할지 물어요.

단계가 끝날 때마다 "이번에 해 드린 것"을 숫자로 한 줄 알려 줘요.

## 알아 둘 점

- **순위는 합격 가능성이 아니라 먼저 볼 순서**예요. 점수도 함께 보여줘요.
- 원티드·링크드인처럼 AI가 직접 열 수 없는 사이트의 공고는, 브라우저를 쓸 수 있는 환경이면 브라우저로 읽어요. 안 되면 공고 내용(주요업무~우대사항)을 복사해 붙여 달라고 요청해요.
- 포트폴리오의 **시각적 완성도는 평가하지 않아요.** 공고와 맞는지, 구성과 내 역할이 잘 보이는지를 봐요.
- 서류 문장을 대신 지어내지 않아요. 제안은 내가 말했거나 서류에 있는 사실 안에서만 해요.

## 개인정보

- 이 레포는 서버가 없고 아무것도 수집하지 않아요. 채팅 내용은 지금 쓰는 ChatGPT·Claude의 정책에 따라 저장돼요.
- 이름, 연락처, 이메일, 주소, 생년월일은 리포트와 커리어 파일에 옮기지 않아요. 그래도 올리기 전에 지우는 게 좋아요.
- 커리어 파일에는 서류 내용이 저장되지 않아요. 다음에 서류 문장을 고칠 때는 서류를 다시 올려 주세요.

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
│   ├── flow-strategy.md      단계 5: 지원 전략 (3Q, 회사별 준비, 행동)
│   ├── flow-feedback.md      단계 6: 지원 결과 기록과 반복 패턴 반영
│   ├── roles.md              직군 4개 정의·검색어·판정 기준
│   ├── ice-rubric.md         점수 기준과 요건 체크리스트
│   ├── score.py              점수·순위 계산
│   ├── career-file.md        커리어 파일 형식
│   └── sample-input.json     score.py 예시 입력
├── i18n/
│   ├── ko/                   한국어 질문·문구·리포트·지원 전략 질문
│   └── en/                   영어 (준비 중)
├── sources.yml               공고 사이트 목록, 사이트별 읽는 방법, 접근 테스트 기록
├── examples/                 테스트용 가상 자료 (디자이너 대화, 이력서, 자소서, 포트폴리오 PDF, 커리어 파일)
└── docs/
    ├── test-checklist.md     규칙을 고친 뒤 확인하는 순서
    └── source-test.md        공고 사이트 접근 테스트 방법
```

## 개발자용

- 점수 계산은 직접 돌려볼 수 있어요.
  ```bash
  python core/score.py core/sample-input.json
  ```
- **브랜치 두 개**: 사용자용 시작 문장은 `stable`을 읽고, 수정과 테스트는 `main`에서 해요. `main`에 push해도 사용자 대화는 바뀌지 않아요. 테스트용 시작 문장은 주소의 `stable`을 `main`으로 바꿔 쓰세요.
- **배포**: [docs/test-checklist.md](docs/test-checklist.md)를 `main`으로 통과한 뒤에만 `git push origin main:stable`로 올려요. 그 순간 사용자 대화에 반영돼요.
- 모든 지침 파일의 마지막 줄은 끝 표시(`<!-- END: 경로 -->`)예요. 에이전트가 파일을 끝까지 읽었는지 확인하는 데 쓰니 지우지 마세요.
- 규칙을 고쳤으면 [docs/test-checklist.md](docs/test-checklist.md) 순서로 확인하세요. 테스트할 때는 AI의 메모리나 과거 대화 참조를 끄세요. 예전 규칙이 기억으로 섞일 수 있어요.

## 라이선스

MIT. [LICENSE](LICENSE)를 보세요.
