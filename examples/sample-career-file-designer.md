# 커리어파일 (테스트용 가상 데이터 · 지원 결과 이어가기)

> 가상 인물의 커리어 파일이에요. `sample-conversation-designer.md`와 같은 인물이 지원 2주쯤 뒤 다시 상담하러 온 상황이에요. 실제 인물·회사와 무관해요.

```career-file
version: 2
updated: 2026-10-05
language: ko

profile:
  roles: [BX 디자이너]
  search_roles: [BX 디자이너]
  current_role: 브랜드 디자이너 (광고 에이전시)
  experience_years: 3년
  career_summary: [브랜드 디자이너 3년 8개월 (광고 에이전시), 프리랜서 그래픽 디자이너 9개월]
  documents: [이력서, 자기소개서]
  salary: 3600만원 이상
  regions: [서울, 경기]
  dealbreakers: []
  interview_checks: [야근]
  education: 4년제 시각디자인
  portfolio: 준비중
  strengths: [로지컬 씽킹, 기획기반의 디자인, 버드아이뷰]
  weaknesses: [수직적인 업무 구조, 수동적인 업무 방식, 하이 퀄리티 디자인]
  confirmed: [roles, search_roles, salary, regions, dealbreakers, interview_checks, education, portfolio, strengths, weaknesses]

story:
  direction: {text: "장기적으로는 브랜드 전략까지 보면서 접점 전반을 디렉팅하는 BX 리드로 성장하고 싶습니다.", evidence: [Q1, 대화 3, 대화 5], status: 확인됨}
  metacognition: {text: "강점은 기획을 먼저 하고 기준을 세우는 힘과 패키지를 인쇄 감리까지 끝낸 경험입니다. 하이 퀄리티 디자인은 완성 기준을 먼저 정하고 감리까지 마친 사례로 보여 줍니다.", evidence: [Q3, 이력서], status: 확인됨}
  consistency: {text: "매체는 달랐지만 매번 여러 접점이 하나의 브랜드로 보이게 하는 기준을 만드는 데 가장 많은 시간을 썼습니다.", evidence: [이력서, 대화 3], status: 확인됨}

postings:
  - id: P1
    company: 샘플코스메틱
    position: BX 브랜드 디자이너
    rank: 1
    role: BX 디자이너
    years_required: 3
    requirements:
      - {text: 관련 경력 3년 이상, type: must, status: met, evidence: "이력서"}
      - {text: 패키지 기획·개발, type: must, status: met, evidence: "이력서: 패키지 3종"}
      - {text: 신규 브랜드 런칭 경험, type: must, status: unmet, evidence: "이력서에 없음"}
    status: 지원
    applied: 2026-10-08
    outcomes: []
  - id: P2
    company: 샘플리테일
    position: BX 디자이너
    rank: 2
    role: BX 디자이너
    years_required: 3
    requirements:
      - {text: 만 3년 이상 시각 디자인 경력, type: must, status: met, evidence: "이력서"}
      - {text: 브랜드 런칭·리브랜딩 리드 경험, type: must, status: partial, evidence: "이력서: 리뉴얼 캠페인 참여"}
      - {text: 공간 브랜딩, type: pref, status: unmet}
    status: 지원
    applied: 2026-10-10
    outcomes: []
  - id: P3
    company: 샘플스튜디오
    position: 브랜드 디자이너 (계약직 12개월)
    rank: 3
    role: BX 디자이너
    status: 관심
    outcomes: []

next_actions:
  - {id: A1, text: 샘플코스메틱 간편 지원 제출, due: 2026-10-08, status: 미확인, result: ""}
  - {id: A2, text: 샘플리테일 지원서 제출, due: 2026-10-10, status: 미확인, result: ""}
  - {id: A3, text: 하루한칸 화면을 사용자 2명에게 보여 주고 막힌 지점 기록, due: 2026-10-12, status: 미확인, result: ""}

learnings: []

history:
  - 2026-10-05: 첫 리포트, BX 디자이너 공고 10개
  - 2026-10-05: 샘플코스메틱 지원 전략
```
