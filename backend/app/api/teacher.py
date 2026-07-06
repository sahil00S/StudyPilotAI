from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.teacher_agent import TeacherAgent

router = APIRouter(
    prefix="/teacher",
    tags=["Teacher"]
)

teacher = TeacherAgent()


class TeacherRequest(BaseModel):
    topic: str


@router.post("/ask")
def ask(req: TeacherRequest):

    answer = teacher.explain(req.topic)

    return {
        "answer": answer
    }