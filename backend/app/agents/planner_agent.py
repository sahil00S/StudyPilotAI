"""
====================================================================
                        STUDYPILOT AI
====================================================================

File: planner_agent.py

Purpose
-------
This agent creates personalized study plans.

Responsibilities
----------------
• Understand user goals
• Generate a study schedule
• Divide topics logically
• Recommend revision days

Uses:
• Gemini Service

Author:
Sahil Sant
====================================================================
"""

from app.services.gemini_service import GeminiService


class PlannerAgent:

    def __init__(self):
        self.gemini = GeminiService()

    def generate_plan(
        self,
        subject,
        exam_date,
        hours_per_day,
        current_level
    ):

        prompt = f"""
You are an expert AI Study Planner.

Create a personalized study plan.

Subject:
{subject}

Exam Date:
{exam_date}

Hours Per Day:
{hours_per_day}

Current Level:
{current_level}

Requirements:

1. Divide topics day-wise.

2. Include revision days.

3. Give motivation tips.

4. Recommend quizzes.

5. Keep the plan practical.

Return the answer in clean markdown.
"""

        return self.gemini.generate(prompt)