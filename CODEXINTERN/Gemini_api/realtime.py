import google.generativeai as genai
from serpapi import GoogleSearch

genai.configure(api_key="AIzaSyBTX_f6pZAThvv_Wwl_7leemWyb_VMI3XQ")

model = genai.GenerativeModel('gemini-2.5-flash')

serpapi_key = "e7920503f73c13704abdc23814e0d2d4be150a0a54fbd089c77d1395c0287fcb"

def google_search(query):
    param = {
        "q": query,
        "hl": "en",
        "gl": "in",
        "api_key": serpapi_key
    }

    search = GoogleSearch(param)
    results = search.get_dict()

    if "organic_results" in results:
        return "\n".join([res["snippet"] for res in results["organic_results"][:5]])
    return "No result Found!"

def chat_with_gemini(query):
    search_result = google_search(query)

    prompt = f""" I searched google for "{query}" and found the following information:
    {search_result}

    Based on this,please give me a concise and to the point answer."""

    response = model.generate_content(prompt)
    return response.text




chat_history = []

while True:
    q = input("You: ")
    chat_history.append(f"User: {q}")
    prompt = "\n".join(chat_history)+"\nAI:"
    response = model.generate_content(prompt)
    #using serpapi for geting realtime info
    if "realtime info" in q.lower():
        q = input("Prompt: ")
        chat_history.append(f"User: {q}")
        r = chat_with_gemini(q)
        print(r)
        chat_history.append(f"AI: {r}")
    else:
        print(response.text)
        chat_history.append(f"AI: {response.text}")
    
    if q.lower() in ["exit","quit"]:
        break