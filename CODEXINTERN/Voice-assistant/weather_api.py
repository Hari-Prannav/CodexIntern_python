import requests

API_KEY = "bee0c458b22c4ae438ec0fd598648dae"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter your city: ")

params = {
    'q': city,
    'appid': API_KEY,
    'units': 'metric'  # You’ll get °C
}

response = requests.get(BASE_URL, params=params)
data = response.json()

temp = data['main']['temp']
weather = data['weather'][0]['main']

print(f"\nCurrent weather in {city}: {temp}°C, {weather}")