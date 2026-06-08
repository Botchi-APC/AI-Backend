from fastapi import FastAPI
from pydantic import BaseModel
from models.survey import SurveyRequest
from services.scoring import calculate_score
from services.personality import determine_type

app = FastAPI()

# 요청 데이터
class SurveyRequest(BaseModel):
    answers: list[int]


# 점수 계산
def calculate_score(answers):
    return {
        "social": sum(answers[0:5]) / 25 * 100,
        "openness": sum(answers[5:10]) / 25 * 100,
        "thinking": sum(answers[10:15]) / 25 * 100,
        "planning": sum(answers[15:20]) / 25 * 100,
        "stability": sum(answers[20:25]) / 25 * 100,
    }


# 유형 결정
def determine_type(scores):
    social = scores["social"]
    planning = scores["planning"]

    if social >= 50 and planning >= 50:
        return "전략가형"

    elif social >= 50 and planning < 50:
        return "탐험가형"

    elif social < 50 and planning >= 50:
        return "분석가형"

    else:
        return "자유인형"


# AI 대신 임시 리포트
def generate_report(scores, personality_type):
    return {
        "type": personality_type,
        "description": f"당신은 {personality_type} 성향을 가지고 있습니다.",
        "strengths": [
            "문제 해결 능력",
            "학습 능력",
            "적응력"
        ]
    }


@app.post("/analyze")
def analyze(data: SurveyRequest):
    if len(data.answers) != 25:
        return {
            "error": "25개의 답변이 필요합니다."
        }

    scores = calculate_score(data.answers)

    personality_type = determine_type(scores)

    report = generate_report(scores, personality_type)

    return {
        "scores": scores,
        "result": report
    }
