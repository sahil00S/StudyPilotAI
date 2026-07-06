from app.services.gemini_service import GeminiService


class FlashcardAgent:

    def __init__(self):
        self.gemini = GeminiService()

    def generate_flashcards(self, topic):

        prompt = f"""
Create flashcards for

{topic}

Format

Q:

A:
"""

        return self.gemini.generate(prompt)