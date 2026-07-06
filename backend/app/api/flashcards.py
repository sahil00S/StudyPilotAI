from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.flashcard_agent import FlashcardAgent

router = APIRouter(
    prefix="/flashcards",
    tags=["Flashcards"]
)

agent = FlashcardAgent()


class FlashcardRequest(BaseModel):
    topic: str


@router.post("/generate")
def generate(req: FlashcardRequest):

    cards = agent.generate_flashcards(req.topic)

    return {
        "flashcards": cards
    }