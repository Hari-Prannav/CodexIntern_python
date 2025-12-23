# Text / Speech to Image Generator

This project converts user input into images using a generative image API. Text prompts are converted into images, and you can optionally capture speech, convert it to text, and then generate an image from that description.[page:1]

## Features

- Accepts a text prompt and sends it to an image generation API.
- Optional voice input:
  - Captures speech from the microphone.
  - Uses speech‑to‑text to convert it to a prompt.
- Saves generated images locally for later viewing.

## Files

- `authtoken.py` – Holds API key or authentication token used to call the image generation API.
- `text_img.py` – Main script that takes text (or converted speech text) and generates an image.

## Requirements

- Python 3.9+
- Typical libraries:
  - `requests` (for API calls)
  - `speechrecognition`, `pyaudio` (if using microphone input)
  - Any other libraries required by the chosen image API client
