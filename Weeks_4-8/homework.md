# Homework 4 — Joseph

## Task 1 — Intro to APIs

https://www.youtube.com/watch?v=hpc5jyVpUpw

This video explains what an API is. You don't need to memorize everything,
just get the general idea: an API is a way for your code to talk to another
computer and get data back.
 
## Setup
In your terminal make sure your venv(virtual environment) is activated with:

source venv/Scripts/activate

After your virtual environment is activated, run:
 
pip install requests
 
If you get any errors, paste them into Claude or ChatGPT and ask why.

What this does is it extracts the environment variable value from the env file. 

## Task 2 

Functions are reusable blocks of code. Master these and everything else gets easier.

```
Check this code out:
a = 1
b = 2
print(a + b)
```
That outputs 5 right?

How would you make it easiar so that it is a function that holds and calls the logic?

Create a new file in your Weeks_4-8 folder called functions.py, this is where you will complete Tasks 2-4

For task 2:

Write a function called add that adds two numbers and prints the result.

Calling the add function should look like:

add(a, b)

Should return the addition of whats in the parameters

## Task 3

Write a function called `multiply(a, b)` that returns the product of two numbers.

## Task 4

Write a function called `is_even(number)` that returns `True` if the number is even and `False` if it's odd.

## Task 5

Create a new file called `jokes.py`.
 
Use the `requests` library to go to this URL:
https://official-joke-api.appspot.com/random_joke
 
This API sends back data that looks like this:
{"type": "general", "setup": "Why did the chicken...", "punchline": "To get to the other side!", "id": 15}
 
That should look familiar — it's just a dictionary!
 
Your job: print the setup and the punchline.
 
Expected output (your joke will be different):
 
Setup: Why don't scientists trust atoms?
Punchline: Because they make up everything!
 
Hints:
- import requests
- Use requests.get() to go to the URL
- Use .json() to turn the response into a dictionary
- Use the dictionary keys to print what you need
 
---

## Task 6 — 

Consult this YT video to figure out how to use the open weather API: https://www.youtube.com/watch?v=NjhrUHBg8rM

ASK CLAUDE if you are confused about certain stuff. 

Consult this YT video to learn what query parameters in APIs are:
https://www.youtube.com/watch?v=qv5XK91OhFo

From everything you learned in the YT video, now proceed with the next few steps:
**Step 2:** In `secrets_practice.py`, ask the user for a city and fetch the current weather using the API.

**Expected output:**

Enter a city: New York
Weather in New York: 72°F, partly cloudy
åå

## Task 7 — Weather App with Menu

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