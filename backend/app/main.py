"""
====================================================================
                        STUDYPILOT AI
====================================================================

File: main.py

Purpose
-------
This is the entry point of the backend.

Responsibilities:
    • Create the FastAPI application
    • Register API routes
    • Start the backend server

Later we will connect:
    • Planner Agent
    • Teacher Agent
    • Quiz Agent
    • Flashcard Agent
    • Revision Agent
    • Memory Agent

Author:
Sahil Sant
====================================================================
"""

from fastapi import FastAPI
from app.api.planner import router as planner_router
from fastapi.middleware.cors import CORSMiddleware
from app.api.teacher import router as teacher_router
from app.api.quiz import router as quiz_router
from app.api.flashcards import router as flash_router
from app.api.chat import router as chat_router





app = FastAPI(
    title="StudyPilot AI",
    description="AI Powered Multi-Agent Study Assistant",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # For hackathon/demo only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(planner_router)
app.include_router(teacher_router)
app.include_router(quiz_router)
app.include_router(flash_router)
app.include_router(chat_router)



@app.get("/")
def home():
    return {
        "status": "Running",
        "project": "StudyPilot AI",
        "message": "Backend is running successfully 🚀"
    }