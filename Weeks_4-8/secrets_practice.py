import os
from dotenv import load_dotenv
import requests

load_dotenv()

secret_word = os.environ.get("SECRET_WORD")
print(f"The secret word is: {secret_word}")


#Task 2


def get_weather(city):
    url: 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "imperial" 
    }

    if response.sta
 