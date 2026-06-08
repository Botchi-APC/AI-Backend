# 🧠 AI Backend (APC_WAI)

FastAPI 기반의 AI 성격 분석 백엔드 서버입니다.

이 프로젝트는 설문 데이터를 입력받아 Upstage LLM을 활용해 사용자 성격을 분석하고 구조화된 JSON 형태로 결과를 반환하는 API 서버입니다.

---

## 🚀 주요 기능

- 설문 응답 기반 성격 분석 API 제공
- 5가지 성향 점수 계산 (social, openness, thinking, planning, stability)
- Upstage LLM을 활용한 개인 맞춤형 성격 리포트 생성
- 구조화된 JSON 응답 제공 (프론트 연동 최적화)
- 예외 처리 및 API 안정성 확보

---

## 🛠️ 기술 스택

- Python 3.12
- FastAPI
- Uvicorn
- Requests
- Upstage LLM API
- python-dotenv

---

## 📁 프로젝트 구조

```
APC_WAI/
├── main.py
├── services/
│   └── ai_agent.py
├── .env
├── .gitignore
├── README.md
```

---

## 🔗 API 명세

### 📌 POST /analyze

사용자 설문 데이터를 기반으로 성격 분석 수행

#### Request

```json
{
  "answers": [1, 2, 3, 4, 5]
}
```

#### Response

```json
{
  "type": "균형형",
  "scores": {
    "social": 54,
    "openness": 61,
    "thinking": 63,
    "planning": 71,
    "stability": 55
  },
  "report": {
    "personality": "",
    "strengths": [],
    "weaknesses": [],
    "relationship_style": "",
    "study_style": "",
    "stress_pattern": "",
    "recommended_environment": ""
  }
}
```

---

## ⚙️ 실행 방법

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## 🧠 아키텍처

```
FastAPI → AI Agent → Upstage API → JSON Response
```

---

## 🚨 트러블슈팅 요약

- 403 Forbidden → API Key 오류
- JSONDecodeError → API 응답 형식 문제
- 500 Error → 예외 처리 부족
- f-string 오류 → JSON 중괄호 escape 문제

---

## 📌 상태

- AI Backend MVP 완료
- 프론트엔드 연동 준비 완료
- 배포 가능 상태
