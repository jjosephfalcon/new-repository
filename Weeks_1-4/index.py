#Importing env package
import os
from dotenv import load_dotenv

#Importing requests package
import requests

load_dotenv()

#Get API key from the env file
API_KEY = os.environ.get("API_KEY")

#Get input from the user for a city
city = input("Enter a city to get the weather: ")

#Makes the API request
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial")
data = response.json()

temp = data["main"]["temp"]
description = data["weather"][0]["description"]

print(f"Weather in {city}: {temp}°F, {description}")