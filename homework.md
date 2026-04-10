# Tech with Tim
https://www.youtube.com/watch?v=VchuKL44s6E&t=33s
Reference this video for 5-10 minutes every day and make progress. For whatever topics on the homework we have jump to sections
in the video that covers it. Also use google or AI to help understand a task.

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
Store your character's topics and responses in a dictionary instead of if/elif.
Example:

responses = {
    "fighting": "Believe it! Never give up!",
    "friendship": "My friends are my power!",
    "food": "I could really go for some ramen right now..."
}

# Homework 3 — Joseph

## Task 1 — Install requests
Open your terminal and run:
```
pip install requests
```

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