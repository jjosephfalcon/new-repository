# Task 1

Task 1 — Look Up Values in a Dictionary

Step 1: Copy this dictionary into your file:

pythonpowers = {
    "Spider-Man": "web-slinging",
    "Thor": "lightning",
    "Hulk": "super strength"
}

Step 2: Print out Thor's power directly using its key.

Step 3: Ask the user for a hero name with input(), then print that hero's power.

Expected output:

Thor's power is lightning

Enter a hero: Hulk
Hulk's power is super strength

# Task 2

Task 2 — Loop Through a Dictionary

Now instead of looking up ONE hero, print ALL of them automatically.

Step 1: Use the same powers dictionary from Task 1.

Step 2: Write a for loop that goes through every hero and prints their name AND their power.

💡 Hint: when you loop over a dictionary, the loop variable gives you the keys one at a time. Then use square brackets to get the value for each key.

Expected output:

Spider-Man's power is web-slinging
Thor's power is lightning
Hulk's power is super strength

# Task 3

Read these documentation articles:

https://realpython.com/python-dicts/

https://realpython.com/python-tuple/

https://mimo.org/glossary/python/set

By next class, explain to me what the difference is between a dictionary, tuple, and set

# Task 4 — HARD MODE: Quiz Game with Full Stats

Build a quiz game. Store 5 questions and answers in a dictionary. Loop through every question, ask the user, and track everything in a stats dictionary.

pythonstats = {
    "answers_given": [],
    "correct": 0,
    "wrong": 0
}

After all 5 questions, print a full report.

Expected output:

What is the capital of France? Paris
Correct!

What is 7 x 8? 56
Correct!

What color is the sky? green
Wrong! The answer was blue.

--- Your Stats ---
Total correct: 2
Total wrong: 1
Your answers: ['Paris', '56', 'green']


💡 Hints:

Store questions as keys, answers as values in one dictionary
Loop through the dictionary with a for loop
Append each user answer to answers_given whether right or wrong
Compare .lower() versions so capitalization doesn't matter