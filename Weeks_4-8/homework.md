# Homework 4 — Joseph

## Task 1 — Bridge to OpenAI - learn what env variables are

Step 1: 

Go on google, and search "What are env variables python". Read an article for 5-10 minutes, if you are stuck 
or confused as ChatGPT.

After that, proceed to the next steps. 

Step 2: 

Create a new file in your directory called ".env", put this line in there:

SECRET_WORD=banana python3 secrets_practice.py

After that reate a new file called `secrets_practice.py`
Inside that file, write this code:

```python
import os
example_secret_word = os.environ.get("SECRET_WORD")
print(f"The secret word is: {secret_word}")
```

What this does is it extracts the environment variable value from the env file. 


## Task 2 — 

Consult this YT video to figure out how to use the open weather API: https://www.youtube.com/watch?v=NjhrUHBg8rM

ASK CLAUDE if you are confused about certain stuff. 

Consult this YT video to learn what query parameters in APIs are:
https://www.youtube.com/watch?v=qv5XK91OhFo

From everything you learned in the YT video, now proceed with the next few steps:
**Step 2:** In `secrets_practice.py`, ask the user for a city and fetch the current weather using the API.

**Expected output:**

Enter a city: New York
Weather in New York: 72°F, partly cloudy


## Task 3 — Weather App with Menu

**Step 1:** Create a function called `get_weather(city)` that takes a city name and returns the weather.

**Step 2:** Add a while loop that:
- Asks the user to input a city name
- Calls `get_weather()` and prints the result
- If the user types "quit", exit the loop

**Expected output:**
```
Enter a city (or quit): Tokyo
Weather in Tokyo: 65°F, sunny

Enter a city (or quit): London
Weather in London: 52°F, rainy

Enter a city (or quit): quit
Goodbye!
```

## Task 4