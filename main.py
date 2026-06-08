from fastapi import FastAPI, HTTPException

from models.survey import SurveyRequest
from services.scoring import calculate_score
from services.personality import determine_type
from services.ai_agent import generate_ai_report

app = FastAPI()


@app.post("/analyze")
def analyze(data: SurveyRequest):

    if len(data.answers) != 25:
        raise HTTPException(400, "25개 필요")

    scores = calculate_score(data.answers)
    personality_type = determine_type(scores)

    ai_report = generate_ai_report(
        scores,
        data.answers,
        personality_type
    )

    return {
        "type": personality_type,
        "scores": scores,
        "report": ai_report
    }