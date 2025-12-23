import speech_recognition as sr
import pyttsx3


recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()


def listen_once(timeout: int = 5, phrase_time_limit: int = 8) -> str:
    """
    Listen from the default microphone once and return recognized text (lowercase).
    Returns empty string on failure.
    """
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source, timeout=timeout,
                                  phrase_time_limit=phrase_time_limit)

    try:
        text = recognizer.recognize_google(audio)
        text = text.lower()
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Network error during speech recognition.")
        return ""


def speak(text: str) -> None:
    """Speak the given text and also print it."""
    if not text:
        return
    print(f"Assistant: {text}")
    tts_engine.say(text)
    tts_engine.runAndWait()
