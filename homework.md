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

## Task 1 — While Loop
Add a while loop to your chatbot so the conversation keeps going until the user types "quit"

**Example output:**
What do you want to talk about? Fighting
Naruto says: Believe it!
What do you want to talk about? quit
Goodbye!

## Task 2 — Add a Function
Move your if/elif response logic into a function called `get_response(topic)`
It should take the topic as input and return the character's response.

## Task 3 — Use dictionaries
Store your character's topics and responses in a dictionary instead of if/elif.
Example:

responses = {
    "fighting": "Believe it! Never give up!",
    "friendship": "My friends are my power!",
    "food": "I could really go for some ramen right now..."
}