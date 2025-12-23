# Gemini API – Chat and Realtime Search

This project implements a Python client for the **Gemini API**, providing an interactive chat interface and (optionally) real‑time search‑augmented responses.

## Features

- Simple command‑line or script‑based chat with the Gemini API.
- Sends user prompts and prints model responses.
- Optional integration of real‑time search results into the prompt for more updated answers.
- Configurable API key and model parameters via environment variables or a config file.

## Requirements

- Python 3.9+
- Typical libraries:
  - `requests` or official `google-generativeai` / `gemini` client
  - `python-dotenv` (if using `.env` files)  
- A valid **Gemini API key**.

Install dependencies (adjust file name if you have a `requirements.txt` here):
