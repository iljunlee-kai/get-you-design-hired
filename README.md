# get-you-hired · 나에게 딱 맞는 직업을 찾아드립니다.

> **English summary** — Upload your AI chat history. The tool asks three short questions, finds 10 matching job postings (Korean market first), scores them with ICE, ranks them S–D, and writes a DOCX report with strengths, weaknesses, blind spots (where what you say differs from how you actually chat) and a 3-day action plan. No server, nothing collected; it runs as a custom GPT or any model that can follow `core/instructions.md`. Work in progress. MIT licensed.


AI와 나눈 대화 기록을 올리면, 나에게 맞는 채용 공고 10개를 찾아 우선순위를 매기고 리포트(DOCX)와 3일 투두를 만들어주는 도구예요.

> 🚧 제작 중이에요. 지금은 **한국 공고만** 지원해요. 샘플 리포트와 바로 쓰기 링크는 준비되는 대로 여기에 들어가요.

## 이런 분께

"내가 어떤 일에 맞는지 모르겠다"는 상태로 이직·취업을 준비하는 분. 정답을 알려주는 도구가 아니라, **내가 한 말과 실제 대화 패턴이 어떻게 다른지** 짚어주고 그 방향에 맞는 공고까지 이어주는 가이드예요.

## 이렇게 동작해요

1. AI와 나눈 대화를 MD 파일로 올려요. (`examples/sample-conversation.md`가 예시예요)
2. AI가 질문 3개를 하나씩 물어요: 원하는 직군·연봉·지역·절대 안 되는 조건 / 학력 / 잘하는 것·어려운 것. 모르겠으면 "잘 모르겠어요"라고 해도 돼요.
3. 조건에 맞는 공고 10개를 찾아요. 게시일과 마감은 페이지에서 읽은 값만 써요. 연봉·야근처럼 공고에 없는 것은 "공고 미기재"로 두고, 야근·문화는 면접에서 물어볼 질문으로 바꿔줘요.
4. 공고마다 ICE(영향·합격 가능성·지원 난이도)로 점수를 매기고 S~D 우선순위를 정해요.
5. 장점·단점·맹점, 공고 리스트, 3일 안에 할 일이 담긴 리포트를 만들어요.

등급은 합격 가능성이 아니라 **이번 후보 중 추천 우선순위**예요. 점수도 함께 보여줘요.

## 개인정보

- 이 레포는 서버가 없고 아무것도 수집하지 않아요.
- 올린 내용은 쓰시는 AI 서비스 안에서만 처리되고, 해당 서비스의 데이터 정책을 따라요.
- 연락처, 실명, 주민번호 같은 정보는 지우고 올려주세요.

## 쓰는 방법

- **ChatGPT**: [gpt/README.md](gpt/README.md)를 따라 커스텀 GPT를 만들어요.
- Claude 버전은 준비 중이에요.

## 폴더 구조

```
├── README.md
├── core/
│   ├── instructions.md   핵심 지침 (모델 중립)
│   ├── ice-rubric.md     ICE 기준표
│   ├── score.py          점수·등급 계산
│   ├── career-file.md    커리어 파일 형식 (세션 간 이어가기)
│   └── sample-input.json
├── i18n/
│   ├── ko/               한국어 질문·문구·리포트 형식
│   └── en/               영어 (준비 중)
├── sources.yml           지역별 허용 공고 사이트
├── gpt/                  ChatGPT 설정 방법
├── examples/             테스트용 가상 대화
└── docs/                 소스 접근 테스트 방법
```

## 개발자용

`core/`는 모델과 언어에 중립이에요. 점수 계산은 직접 돌려볼 수 있어요.

```bash
python core/score.py core/sample-input.json
```

수정은 항상 `core/`와 `i18n/`에서 하고, GPT 같은 래퍼에는 복사해서 써요.

## 라이선스

MIT. [LICENSE](LICENSE)를 보세요.
