import google.generativeai as genai

genai.configure(api_key="AIzaSyBTX_f6pZAThvv_Wwl_7leemWyb_VMI3XQ")

model = genai.GenerativeModel('gemini-2.5-flash')

chat_history = []

while True:
    q = input("You: ")
    chat_history.append(f"User: {q}")
    prompt = "\n".join(chat_history)+"\nAI:"
    response = model.generate_content(prompt)
    chat_history.append(f"AI: {response.text}")
    print(response.text)
    if q.lower() in ["exit","quit"]:
        break



