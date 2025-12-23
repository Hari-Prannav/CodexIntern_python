import os
import requests

from config import WEATHER_API_KEY

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city: str) -> str:
    """Return a human-readable weather sentence for the given city."""
    if not WEATHER_API_KEY:
        return "Weather API key is not configured."

    try:
        params = {
            "q": city,
            "appid": WEATHER_API_KEY,
            "units": "metric",
        }
        resp = requests.get(BASE_URL, params=params, timeout=5)
        resp.raise_for_status()
        data = resp.json()

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        feels_like = data["main"].get("feels_like", temp)

        return (
            f"The current temperature in {city} is {temp:.1f}°C, "
            f"feels like {feels_like:.1f}°C, with {desc}."
        )
    except Exception:
        return "I could not fetch the weather right now."
