from datetime import datetime

from speech_text import listen_once, speak
from weather_api import get_weather


WAKE_WORDS = ["assistant", "hey assistant"]


def handle_command(text: str) -> None:
    """
    Handle a single command string (text without wake word).
    Extend this with more intents over time.
    """
    if not text:
        speak("I did not hear any command.")
        return

    # Simple weather intent
    if "weather" in text:
        speak("Which city?")
        city = listen_once()
        if city:
            response = get_weather(city)
            speak(response)
        else:
            speak("I did not hear the city name.")
        return

    # Time intent
    if "time" in text:
        now = datetime.now().strftime("%H:%M")
        speak(f"The time is {now}.")
        return

    # You can add more commands here (date, jokes, wiki, etc.)

    # Default fallback
    speak("I can tell you the time or the weather. Try asking for one of those.")


def main() -> None:
    speak("Hello, I am your voice assistant. Say 'assistant' followed by a command.")

    while True:
        text = listen_once()

        # Exit commands work even without wake word
        if any(word in text for word in ["stop", "exit", "quit"]):
            speak("Goodbye!")
            break

        # Only react when wake word is detected
        if any(w in text for w in WAKE_WORDS):
            for w in WAKE_WORDS:
                text = text.replace(w, "").strip()
            if not text:
                speak("Yes? What do you want me to do?")
                text = listen_once()
            handle_command(text)
        else:
            # Ignore other noise/phrases
            pass


if __name__ == "__main__":
    main()
