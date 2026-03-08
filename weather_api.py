import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env for development convenience
load_dotenv()

# Expect the weather API key in the environment variable `WEATHER_API_KEY`.
API_KEY = os.environ.get('WEATHER_API_KEY')
if not API_KEY:
    # Raise at import time to make missing-config obvious in development.
    raise RuntimeError('Environment variable WEATHER_API_KEY is not set. Please add it to your .env or export it.')

def getCurrWeather(loc):
    location = loc
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={location}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        current_weather = data['current']
        return current_weather['temp_c'], current_weather['condition']['text'], current_weather['humidity'], current_weather['wind_kph']
    else:
        return None