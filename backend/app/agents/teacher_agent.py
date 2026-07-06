from app.services.gemini_service import GeminiService


class TeacherAgent:

    def __init__(self):
        self.gemini = GeminiService()

    def explain(self, topic):

        prompt = f"""
You are an expert AI Teacher.

Explain {topic} to a beginner.

Use simple language.

Give examples.

End with 3 practice questions.
"""

        return self.gemini.generate(prompt)