#Importing env package
import os
from dotenv import load_dotenv

#Importing requests package
import requests

load_dotenv()

#Get API key from the env file
API_KEY = "3082ba1f5cf471c8d8ece072a3ea8f81"

#
city = input("Enter a city to get the weather: ")

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial")
data = response.json()

temp = data["main"]["temp"]
description = data["weather"][0]["description"]

print(f"Weather in {city}: {temp}°F, {description}")