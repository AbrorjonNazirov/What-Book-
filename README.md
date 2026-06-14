# 📚 Mood-Driven AI Librarian

## 1. Project Objective and Role
**Status:** Capstone Requirement | **Role:** Architect & Lead Engineer

This project demonstrates modern software engineering skills by combining Python with Generative AI. It is a Go-To-Market (GTM) ready web application that acts as a personal AI librarian. By analyzing user mood, pacing preferences, and narrative desires through a dynamic questionnaire, the application leverages Google's Gemini AI to provide structured, highly tailored book recommendations.

## 2. Technical Requirements & Core Technologies
- **Language:** Python 3.10+
- **Framework:** Streamlit (for a sleek, portable web UI)
- **GenAI Orchestration:** `google-genai` (Gemini 2.5 Flash)
- **Data Validation:** Pydantic (ensures the LLM returns strictly structured JSON data)
- **Architecture:** Modular, clean code separating UI (`app.py`), configuration (`config.py`), and LLM logic (`llm_service.py`). Includes a GTM-ready fallback mechanism for offline functionality.

## 3. Portability and Execution Standards

### Prerequisites
- Python 3.10 or higher.
- A valid Google Gemini API Key.

### Installation
Clone the repository and install the required dependencies via the terminal:
```bash
pip install -r requirements.txt