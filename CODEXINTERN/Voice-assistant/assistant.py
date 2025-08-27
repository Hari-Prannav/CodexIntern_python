import speech_recognition as sr
import pyttsx3
import requests
import datetime

engine = pyttsx3.init()
print("Assistant: Hello! I'm your personal assistant. How can I help you today?")
engine.say("Hello! I'm your personal assistant. How can I help you today?")
engine.runAndWait()

recognizer = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Speak now...")

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = recognizer.recognize_google(audio, language="en-US")
            print("You:", text)
        except sr.UnknownValueError:
            print("Assistant: Sorry, I can't hear you")
            engine.say("Sorry, I can't hear you")
            engine.runAndWait()
            text = ""
            continue 

        if "weather" in text.lower():
            city = "Chennai"
            api_key = "bee0c458b22c4ae438ec0fd598648dae"
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                temp = data['main']['temp']
                weather = data['weather'][0]['description']
                print(f"\nAssistant: Current weather in {city}: {temp}°C, {weather}")
                engine.say(f"The weather in {city} is {weather} with a temperature of {temp} degrees Celsius")
                engine.runAndWait()
            else:
                print("Assistant: Sorry, I couldn't fetch the weather!")
                engine.say("Sorry, I couldn't fetch the weather!")
                engine.runAndWait()
        
        elif "news" in text.lower():
            api_key_news = "117e5c4c993f459bb940412b32ef1185"
            url_news = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key_news}"
            response = requests.get(url_news)
            if(response.status_code == 200):
                articles = response.json().get("articles",[])
                headlines = [article['title'] for article in articles[:5]]
                print("Assistant: Here are the top 5 Headline news in US: ")
                for i,headline in enumerate(headlines,1):
                    print(f"{i}. {headline}")
                engine.say("Here are the top 5 Headline news in US: "+",".join(headlines))
                engine.runAndWait()

        elif "time" in text:
            time = datetime.datetime.now().strftime("%I:%M %p")
            print(f"Assistant: The current time is: {time}")
            engine.say(f"The current time is: {time}.")
            engine.runAndWait()


        elif "exit" in text.lower() or "quit" in text.lower():
            print("Assistant: Goodbye!")
            engine.say("Goodbye! Have a nice day.")
            engine.runAndWait()
            break

        else:
            print("Assistant: I'm not sure how to help with that.")
            engine.say("I'm not sure how to help with that.")
            engine.runAndWait()
