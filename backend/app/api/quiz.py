from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.quiz_agent import QuizAgent

router = APIRouter(
    prefix="/quiz",
    tags=["Quiz"]
)

quiz = QuizAgent()


class QuizRequest(BaseModel):
    topic: str


@router.post("/generate")
def generate(req: QuizRequest):

    result = quiz.generate_quiz(req.topic)

    return {
        "quiz": result
    }