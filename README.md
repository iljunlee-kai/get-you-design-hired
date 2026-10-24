# get-you-design-hired · 디자인 커리어

> **English summary** — A personal job-search agent that gets to know you from your AI chat history. Upload your chats; it asks three short questions, tells you what kind of person and which roles your conversations point to (with evidence), finds 10 matching job postings (Korean market first, tuned for four design roles: product, content, BX and brand designers), scores them with ICE, ranks them 1–10, and writes a DOCX report with strengths, weaknesses, blind spots and a 3-day action plan. Save the career file it gives you; next time it won't re-ask what it already knows and starts by asking how your last actions went. No server, nothing collected; the agent reads this repo directly, starting from `START.md` (custom GPT or any AI that can browse). Work in progress. MIT licensed.


AI와 나눈 대화 기록으로 나를 알아가는 **나만의 취업 도우미**예요. 대화에서 보이는 내 모습과 어울리는 직업을 짚어주고, 나에게 맞는 채용 공고 10개의 우선순위와 리포트(DOCX), 3일 투두를 만들어줘요. 저장해 둔 커리어 파일을 다시 올리면 처음부터 묻지 않고, 지난번에 하기로 한 일부터 이어서 상담해요.

지금은 **프로덕트 디자이너, 콘텐츠 디자이너, BX 디자이너, 브랜드 디자이너** 직군에 맞춰 다듬고 있어요.

> 🚧 제작 중이에요. 지금은 **한국 공고만** 지원해요. 샘플 리포트와 바로 쓰기 링크는 준비되는 대로 여기에 들어가요.

## 이런 분께

"내가 어떤 일에 맞는지 모르겠다"는 상태로 이직·취업을 준비하는 분. 정답을 알려주는 도구가 아니라, **내가 한 말과 실제 대화 패턴이 어떻게 다른지** 짚어주고 그 방향에 맞는 공고까지 이어주는 가이드예요.

## 이렇게 동작해요

1. AI와 나눈 대화를 MD 파일로 올려요. 이력서와 자기소개서가 있으면 같이 올려요 (선택). (`examples/`의 `sample-conversation.md`(마케터)와 `sample-conversation-designer.md`(디자이너)가 예시예요)
2. AI가 질문 3개를 하나씩 물어요: 원하는 직군·연봉·지역·절대 안 되는 조건 / 학력 / 잘하는 것·어려운 것. 모르겠으면 "잘 모르겠어요"라고 해도 돼요.
3. 조건에 맞는 공고 10개를 찾아요. 게시일과 마감은 페이지에서 읽은 값만 써요. 연봉·야근처럼 공고에 없는 것은 "공고 미기재"로 두고, 야근·문화는 면접에서 물어볼 질문으로 바꿔줘요.
4. 공고마다 ICE(영향·합격 가능성·지원 난이도)로 점수를 매기고 1~10위 순서를 정해요.
5. 장점·단점·맹점, "대화에서 보이는 나"와 어울리는 직업, 공고 리스트, 3일 안에 할 일이 담긴 리포트를 만들어요.
6. 마지막에 나오는 커리어 파일을 저장해 두세요. 다음에 올리면 이미 말한 내용은 다시 묻지 않고, 지난번에 하기로 한 일이 어떻게 됐는지부터 이어서 얘기해요.

순위는 합격 가능성이 아니라 **이번 후보 중 먼저 볼 순서**예요. 점수도 함께 보여줘요.

## 개인정보

- 이 레포는 서버가 없고 아무것도 수집하지 않아요.
- 올린 내용은 쓰시는 AI 서비스 안에서만 처리되고, 해당 서비스의 데이터 정책을 따라요.
- 연락처, 실명, 주민번호 같은 정보는 지우고 올려주세요.

## 쓰는 방법

에이전트가 이 레포를 직접 읽어요. 시작 파일은 [`START.md`](START.md)예요. `main`에 올린 내용이 바로 반영돼요.

- **ChatGPT**: [gpt/README.md](gpt/README.md)대로 커스텀 GPT를 만들어요. 지침 칸에는 시작 방법 몇 줄만 넣어요.
- **Claude 등 웹을 읽을 수 있는 AI**: 새 대화에서 이렇게 시작해요.

```
https://github.com/iljunlee-kai/get-you-hired 의 START.md를 읽고 그대로 진행해줘.
```

## 폴더 구조

```
├── README.md
├── START.md                에이전트 시작 파일 (흐름과 읽을 파일 목록)
├── core/
│   ├── principles.md       원칙·정지 지점·금지
│   ├── flow-intake.md      단계 1: 시작·질문·프로필
│   ├── flow-search-score.md 단계 2: 공고 검색·채점·순위
│   ├── flow-report.md      단계 3: 리포트·재실행
│   ├── flow-resume.md      단계 4: 커리어 파일·이어가기
│   ├── roles.md            직군 4개 정의·검색어·판정 기준
│   ├── ice-rubric.md       ICE 기준표
│   ├── score.py            점수·순위 계산
│   ├── career-file.md      커리어 파일 형식
│   └── sample-input.json
├── i18n/
│   ├── ko/                 한국어 질문·문구·리포트 형식
│   └── en/                 영어 (준비 중)
├── sources.yml             지역별 허용 공고 사이트
├── gpt/                    ChatGPT 설정 방법과 지침 문구
├── examples/               테스트용 가상 대화
└── docs/                   소스 접근 테스트 방법
```

## 개발자용

`core/`는 모델과 언어에 중립이에요. 점수 계산은 직접 돌려볼 수 있어요.

```bash
python core/score.py core/sample-input.json
```

수정은 `START.md`, `core/`, `i18n/`에서 해요. 에이전트가 레포를 직접 읽으니 복사본을 따로 관리하지 않아요. 모든 지침 파일의 마지막 줄은 끝 표시(`END`)예요. 파일을 고칠 때 지우지 마세요.

## 라이선스

MIT. [LICENSE](LICENSE)를 보세요.
