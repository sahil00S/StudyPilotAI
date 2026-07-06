"""
====================================================================
                        STUDYPILOT AI
====================================================================

File: gemini_service.py

Purpose
-------
This service is the ONLY place that communicates with Google Gemini.

Why?

Instead of every agent talking directly to Gemini, all agents use
this service.

Benefits:
• Clean architecture
• Easy maintenance
• Reusable code
• One place to change model settings

Used By:
• Planner Agent
• Teacher Agent
• Quiz Agent
• Flashcard Agent
• Revision Agent

Author:
Sahil Sant
====================================================================
"""

from google import genai
from app.config import GEMINI_API_KEY


class GeminiService:
    """
    Handles all communication with the Gemini API.
    """

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate(self, prompt: str) -> str:
        """
        Send a prompt to Gemini and return the generated text.
        """

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text