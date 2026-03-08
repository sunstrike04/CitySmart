import os
import requests
from dotenv import load_dotenv

# Load a local .env during development so I can keep keys out of git
load_dotenv()

# Weather API key should be in WEATHER_API_KEY; fail fast if it's not set
API_KEY = os.environ.get('WEATHER_API_KEY')
if not API_KEY:
    raise RuntimeError('WEATHER_API_KEY is not set. Add it to .env or export it in your shell.')

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