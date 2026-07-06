"""
====================================================================
                        STUDYPILOT AI
====================================================================

File: config.py

Purpose
-------
This file is responsible for loading all configuration values
used throughout the backend.

Instead of hardcoding API keys or secrets inside the code,
we store them in a .env file and load them from here.

Current Configuration:
    • Gemini API Key

Future Configuration:
    • Database URL
    • JWT Secret Key
    • Application Settings

Why?
----
Keeping configuration separate makes the application
secure, clean, and easy to maintain.

Author:
Sahil Sant
====================================================================
"""

import os
from dotenv import load_dotenv

# --------------------------------------------------------------
# Load all variables from backend/.env
# --------------------------------------------------------------
load_dotenv()

# --------------------------------------------------------------
# Gemini API Key
# --------------------------------------------------------------
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# --------------------------------------------------------------
# Verify API Key Exists
# --------------------------------------------------------------
if GEMINI_API_KEY is None:
    raise ValueError(
        "GEMINI_API_KEY not found. Please check your backend/.env file."
    )