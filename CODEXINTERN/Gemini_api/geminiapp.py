import os
import google.generativeai as genai

# set env var GEMINI_API_KEY before running
genai.configure(api_key=os.environ["AIzaSyDe2T2c1XrwgJH52F1Aj7hh9IROq6yN5yM"])

model = genai.GenerativeModel("gemini-2.5-flash")

chat_history = []

while True:
    q = input("You: ")
    chat_history.append(f"User: {q}")
    prompt = "\n".join(chat_history) + "\nAI:"
    response = model.generate_content(prompt)
    chat_history.append(f"AI: {response.text}")
    print(response.text)

    if q.lower() in ["exit", "quit"]:
        break
