from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models.survey import SurveyRequest
from services.scoring import calculate_score
from services.personality import determine_type
from services.ai_agent import generate_ai_report
from data.questions import QUESTIONS


app = FastAPI()

origins = [
    "http://localhost:5175",  # Vite 기본
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/analyze")
def analyze(data: SurveyRequest):

    if len(data.answers) != 25:
        raise HTTPException(status_code=400, detail="25개 필요")

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

@app.get("/questions")
def get_questions():
    return QUESTIONS