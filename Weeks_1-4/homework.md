# Tech with Tim
https://www.youtube.com/watch?v=VchuKL44s6E&t=33s
Reference this video for 5-10 minutes every day and make progress. For whatever topics on the homework we have jump to sections
in the video that covers it. Also use google or AI to help understand a task.

-----------------------------------------------------------------------------------------------------------------------------------
# Homework 1 — Joseph(done)

## Task 1 — Code
In `index.py`, write a program that asks the user their name AND their favorite character, then prints a greeting using both.

**Example output:**
```
What's your name? Joseph
Who's your favorite character? Naruto
Nice to meet you Joseph! Get ready to talk to Naruto..
```

## Task 2 — Game Description
Add to your `index.py` program — after greeting the user, ask them what they want to talk about and print a response.

**Example output:**
```
What's your name? Joseph
Who's your favorite character? Naruto
Nice to meet you Joseph! Get ready to talk to Naruto...
What do you want to talk about? Fighting
Naruto says: Believe it! Never give up!
```

## Bonus Task (Hard) — If you dare 🔥
Try adding an `if/elif/else` statement so the response changes based on what topic they pick.

**Example output:**
```
What do you want to talk about? Fighting
Naruto says: Believe it! Never give up!

What do you want to talk about? Friendship
Naruto says: My friends are my power!

What do you want to talk about? Food
Naruto says: I could really go for some ramen right now...
```
-----------------------------------------------------------------------------------------------------------------------------------
# Homework 2 — Joseph

## Task 1 — Redo Task One
At the start, let the user pick from a list of characters(pick your 5 favorite). 
How this works
-You hardcode your 5 characters into an array at the top of the 
Return an error and quit the program if the users response for a character is not in that list.

## Task 2 — While Loop
Add a while loop to your chatbot so the conversation keeps going until the user types "quit"

**Example output:**
What do you want to talk about? Fighting
Naruto says: Believe it!
What do you want to talk about? quit
Goodbye!

## Task 3 — Add a Function
Move your if/elif response logic into a function called `get_response(topic)`
It should take the topic as input and return the character's response.

## Task 4 — Use dictionaries
Store your character's topics and responses in a dictionary instead of if/elif statements.
Example:

responses = {
    "fighting": "Believe it! Never give up!",
    "friendship": "My friends are my power!",
    "food": "I could really go for some ramen right now..."
}



-----------------------------------------------------------------------------------------------------------------------

# Homework 3 — Joseph

## Task 1 — Install requests
Go on google and search basic documentation, something like "intro to API's", 
This video can also be helpful: https://www.youtube.com/watch?v=hpc5jyVpUpw
Try to get into the habit of self learning with resources online, even ask Claude or ChatGPT. 

Open your terminal and run:
```
pip install requests
```
If you get any bugs, ask ChatGPT/Claude why. 

## Task 2 — Fetch from an API
Create a new file called `jokes.py`. Use the `requests` library to fetch a random joke from this free API:
```
https://official-joke-api.appspot.com/random_joke
```
Print the setup and punchline.

**Example output:**
```
Setup: Why don't scientists trust atoms?
Punchline: Because they make up everything!
```


## Task 3 — Loop it
Add a while loop — every time the user presses Enter, fetch a new joke. Quit when they type "quit".

**Example output:**
```
Press Enter for a joke (or type quit): 
Setup: Why did the scarecrow win an award?
Punchline: Because he was outstanding in his field!

Press Enter for a joke (or type quit): 
Setup: What do you call a fake noodle?
Punchline: An impasta!

Press Enter for a joke (or type quit): quit
Goodbye!
```

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

