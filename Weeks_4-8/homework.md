# Task 1 — Movie Directors

Step 1: Create a dictionary called movies that stores at least 5 movie titles and their directors.
Create a second dictionary called genres that stores those same 5 movie titles and their genre (Action, Comedy, Horror, etc.)

Step 2: Define a function called get_movie_info(title) that takes a movie title and returns a formatted string with both the director AND the genre. If the title isn't in the dictionary, return "Never heard of it!".
–
💡 Hint: look up the title in both dictionaries separately, then combine the results into one string using an f-string.

Step 3: Write a while loop that asks the user to enter a movie title. If they type "quit", print "Goodbye!" and break. Otherwise, call get_movie_info() and print the result.

Expected output:

Enter a movie (or quit): Inception

Director: Christopher Nolan | Genre: Sci-Fi

Enter a movie (or quit): The Shining

Director: Stanley Kubrick | Genre: Horror

Enter a movie (or quit): Shrek

Never heard of it!

Enter a movie (or quit): quit

Goodbye!

# Task 2

Number Guessing with Basic Dictionary

Computer picks a number 1–20. User gets 3 attempts. Track just two things:

pythonstats = {
    "attempts": 0,
    "won": False
}

Expected output:
Guess a number (1-20): 10
Too high!
Guess a number (1-20): 5
Too low!
Guess a number (1-20): 7
You got it!

--- Stats ---
Attempts used: 3
Won: True

# Task 3

Challenge 3 HARD MODE — Number Guessing with Stats Tracker

The computer picks a random number 1–100. The user gets unlimited guesses but you track everything in a dictionary and print a full stats report at the end.

pythonstats = {
    "guesses": [],
    "total_attempts": 0,
    "won": False
}

Expected output:

Guess a number (1-100): 50

Too high!

Guess a number (1-100): 25

Too low!

Guess a number (1-100): 37

You got it!

--- Your Stats ---

Total attempts: 3

Your guesses: [50, 25, 37]

Won: True