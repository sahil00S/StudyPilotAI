from app.services.gemini_service import GeminiService


class QuizAgent:

    def __init__(self):
        self.gemini = GeminiService()

    def generate_quiz(self, topic):

        prompt = f"""
Create 10 MCQs on

{topic}

Return:

Question

4 options

Correct answer

Difficulty
"""

        return self.gemini.generate(prompt)