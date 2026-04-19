"""
characters = ["naruto", "goku", "luffy", "eren", "tanjiro"]

print("hello world!")
name = input("whats your name? ")

# Show available characters
print("Available characters:", characters)
character = input("whats your fav character? ")

# Validate character choice
if character.lower() not in characters:
    print("Error: That character is not available. Goodbye!")
    quit()

age = input("how old are you? ")
print(f"Nice to meet you, {name}! You are {age} years old.")
print(f"Get ready to talk to {character}!")

# Task 4 — Dictionary instead of if/elif
responses = {
    "fighting": "I love fighting! It's so exciting and adrenaline-pumping!",
    "cooking": "Cooking is one of my favorite hobbies! I love trying new recipes.",
    "traveling": "Traveling is amazing! I love exploring new places and cultures.",
    "music": "Music is life! I could listen to it all day long.",
    "gaming": "Gaming is so fun! What's your favorite game?"
}
def get_response(topic):
    topic_lower = topic.lower()
    if topic_lower in responses:
        return responses[topic_lower]
    else:
        return f"{topic} is an interesting topic! I enjoy talking about it too."

# Task 2 — While loop until "quit"
while True:
    topic = input("what do you want to talk about? ")
    if topic.lower() == "quit":
        print("Goodbye!")
        break
    character_response = get_response(topic)
    print(f"{character} says: {character_response}")

print(f"Thanks for chatting, {name}! Come back soon.")
"""
import requests
from dotenv import load_dotenv
import os

load_dotenv()

# Task 1
secret_word = os.environ.get("SECRET_WORD")


# Task 2
def get_weather(city):
    api_key = os.environ.get("API_KEY")
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "imperial"
    }
    response = requests.get(url, params=params)
    data = response.json()

    if "main" not in data:
        return f"City '{city}' not found. Please check the spelling."

    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    return f"Weather in {city}: {temp}°F, {description}"

# Task 3
while True:
    city = input("\nEnter a city (or quit): ")
    if city.lower() == "quit":
        print("Goodbye!")
        break
    print(get_weather(city))