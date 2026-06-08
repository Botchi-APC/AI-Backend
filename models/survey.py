from pydantic import BaseModel

class SurveyRequest(BaseModel):

    answers: list[int]