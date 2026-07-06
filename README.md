# 🎓 StudyPilot AI

> An AI-powered Multi-Agent Study Assistant built with FastAPI and Google Gemini.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Gemini](https://img.shields.io/badge/Google-Gemini-orange)
![License](https://img.shields.io/badge/License-MIT-red)

---

# 📌 Overview

StudyPilot AI is a multi-agent educational assistant designed to help students learn more effectively using Artificial Intelligence.

Instead of acting as a simple chatbot, StudyPilot AI contains multiple specialized AI agents, each responsible for a different learning task such as planning, teaching, quiz generation, flashcard generation, and academic assistance.

This project was developed as part of the Kaggle **AI Agents: Intensive Vibe Coding Capstone**.

---

# ✨ Features

## 📅 AI Study Planner
- Generates personalized study plans
- Creates day-wise schedules
- Adds revision days
- Motivational study tips
- Practical learning roadmap

---

## 👨‍🏫 AI Teacher

- Explains difficult topics
- Beginner-friendly explanations
- Uses real-life examples
- Provides practice questions

---

## 📝 AI Quiz Generator

- Generates MCQs instantly
- Includes correct answers
- Adjustable difficulty
- Topic-based quizzes

---

## 🧠 AI Flashcard Generator

- Generates revision flashcards
- Question & Answer format
- Perfect for active recall

---

## 💬 AI Study Chat

Students can ask anything such as:

- Explain CNN
- Explain RNN
- Difference between AI and ML
- Mathematics
- Programming
- Exam preparation

Powered by Google Gemini.

---

# 🏗️ Architecture

```
                    Frontend (HTML/CSS/JS)
                              │
                              │
                              ▼
                       FastAPI Backend
                              │
        ┌─────────────────────┼──────────────────────┐
        │                     │                      │
        ▼                     ▼                      ▼
 Planner Agent          Teacher Agent         Quiz Agent
        │                     │                      │
        └──────────────┬──────┴──────────────┬───────┘
                       ▼
                 Gemini Service
                       │
                       ▼
               Google Gemini API
```

---

# 🛠️ Tech Stack

### Backend

- FastAPI
- Python
- Google Gemini API
- Pydantic

### Frontend

- HTML
- CSS
- Bootstrap
- JavaScript

---

# 📂 Project Structure

```
StudyPilotAI/

│

├── backend/

│   ├── app/

│   │   ├── agents/

│   │   ├── api/

│   │   ├── services/

│   │   ├── schemas/

│   │   ├── database/

│   │   ├── utils/

│   │   ├── config.py

│   │   └── main.py

│

├── frontend/

│   ├── assets/

│   ├── dashboard/

│   ├── index.html

│   └── ...

│

├── README.md

└── requirements.txt
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/sahil00S/StudyPilotAI.git
```

Go inside

```bash
cd StudyPilotAI/backend
```

Install packages

```bash
pip install -r requirements.txt
```

Create `.env`

```
GEMINI_API_KEY=YOUR_API_KEY
```

Run

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

# 📷 Screenshots

- Home Page
- Planner
- AI Chat
- Quiz
- Flashcards
- Swagger API

(Add screenshots here.)

---

# 🔮 Future Improvements

- PDF syllabus upload
- OCR support
- User authentication
- Progress tracking
- Revision reminders
- Calendar integration
- Voice assistant
- Mobile application

---

# 👨‍💻 Team

**Backend & AI**

Sahil Sant

- FastAPI
- AI Agents
- Google Gemini
- API Development

**Frontend**

(Your Friend's Name)

- HTML
- CSS
- Bootstrap
- JavaScript

---

# 🙏 Acknowledgements

- Google Gemini
- Kaggle
- FastAPI
- Bootstrap
- Python Community

---

# 📄 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider giving it a star.
