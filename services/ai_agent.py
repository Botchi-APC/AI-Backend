import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

API_KEY = os.getenv("UPSTAGE_API_KEY")


def generate_ai_report(scores, answers, personality_type):

    url = "https://api.upstage.ai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
        너는 전문 성격 분석 AI이다.

        성격 유형: {personality_type}
        점수: {scores}
        응답: {answers}

        아래를 개인 맞춤형으로 분석해라:

        1. 성격 특징
        2. 강점 3개
        3. 약점 3개
        4. 인간관계 스타일
        5. 공부/업무 스타일
        6. 스트레스 반응
        7. 추천 환경

        절대 템플릿처럼 쓰지 말고 사람 한 명 분석하듯 작성

        반드시 JSON 형식으로 출력해라:

        {{
        "personality": "",
        "strengths": [],
        "weaknesses": [],
        "relationship_style": "",
        "study_style": "",
        "stress_pattern": "",
        "recommended_environment": ""
        }}
        """

    data = {
        "model": "solar-mini",
        "messages": [
            {"role": "system", "content": "너는 심리 분석 전문가다."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4,
        "max_tokens": 1200
    }

    # 디버깅용 (중요)
    response = requests.post(url, json=data, headers=headers)

    print("STATUS:", response.status_code)
    print("TEXT:", response.text)

    if response.status_code != 200:
        return "AI 분석 실패 (API 오류)"

    content = response.json()["choices"][0]["message"]["content"]

    try:
        return json.loads(content)
    except:
        return {"report": content}