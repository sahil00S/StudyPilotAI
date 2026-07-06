"""
====================================================================
                        STUDYPILOT AI
====================================================================

File: planner_schema.py

Purpose
-------
Defines the structure of data received by the Planner Agent.

Why use Pydantic?

• Automatically validates user input.
• Prevents missing fields.
• Generates API documentation automatically.
• Makes the backend more secure.

Author:
Sahil Sant
====================================================================
"""

from pydantic import BaseModel, Field


class PlannerRequest(BaseModel):
    """
    Data sent by the frontend to generate a study plan.
    """

    subject: str = Field(..., description="Subject to study")

    exam_date: str = Field(..., description="Exam date")

    hours_per_day: int = Field(
        ...,
        gt=0,
        description="Hours available every day"
    )

    current_level: str = Field(
        ...,
        description="Student skill level"
    )