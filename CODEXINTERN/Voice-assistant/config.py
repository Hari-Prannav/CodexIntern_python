import os

# Set these environment variables in your OS, do NOT hard-code keys in code.
# Example (PowerShell):
#   setx WEATHER_API_KEY "your_openweather_key"

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "")
