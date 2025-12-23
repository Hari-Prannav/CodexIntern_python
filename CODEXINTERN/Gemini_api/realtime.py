import os
import google.generativeai as genai
from serpapi import GoogleSearch

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash")

serpapi_key = os.environ["SERPAPI_API_KEY"]


def google_search(query: str) -> str:
    params = {
        "q": query,
        "hl": "en",
        "gl": "in",
        "api_key": serpapi_key,
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    if "organic_results" in results:
        return "\n".join(
            res.get("snippet", "")
            for res in results["organic_results"][:5]
            if "snippet" in res
        )
    return "No result found!"


def chat_with_gemini(query: str) -> str:
    search_result = google_search(query)
    prompt = f"""I searched Google for "{query}" and found the following information:
{search_result}

Based on this, please give me a concise and to-the-point answer."""
    response = model.generate_content(prompt)
    return response.text


chat_history: list[str] = []

while True:
    q = input("You: ")
    chat_history.append(f"User: {q}")
    prompt = "\n".join(chat_history) + "\nAI:"
    response = model.generate_content(prompt)

    if "realtime info" in q.lower():
        q2 = input("Prompt: ")
        chat_history.append(f"User: {q2}")
        r = chat_with_gemini(q2)
        print(r)
        chat_history.append(f"AI: {r}")
    else:
        print(response.text)
        chat_history.append(f"AI: {response.text}")

    if q.lower() in ["exit", "quit"]:
        break
