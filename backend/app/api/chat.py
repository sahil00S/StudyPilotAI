from fastapi import APIRouter
from pydantic import BaseModel
from app.services.gemini_service import GeminiService

router = APIRouter(
    prefix="/chat",
    tags=["AI Chat"]
)

gemini = GeminiService()


class ChatRequest(BaseModel):
    message: str


@router.post("/")
def chat(req: ChatRequest):

    answer = gemini.generate(req.message)

    return {
        "response": answer
    }