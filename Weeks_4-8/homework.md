# Task 1 — Football Players

Step 1: Create a dictionary called players that stores at least 5 football player names and their club/team. Create a second dictionary called positions that stores those same 5 players and their position (Forward, Midfielder, Defender, etc.)

Step 2: Define a function called get_player_info(name) that takes a player name and returns a formatted string with both the club AND the position. If the name isn't in the dictionary, return "Player not found!"


💡 Hint: look up the name in both dictionaries separately, then combine with an f-string.

Step 3: Write a while loop that asks the user to enter a player name. If they type "quit", print "See you next match!" and break. Otherwise, call get_player_info() and print the result.

Expected output:

Enter a player (or quit): Messi
Club: Inter Miami | Position: Forward

Enter a player (or quit): Ronaldo
Club: Al-Nassr | Position: Forward

Enter a player (or quit): LeBron
Player not found!

Enter a player (or quit): quit
See you next match!


# Task 2 — Password Checker with Dictionary

The user gets 3 attempts to guess the correct password. Track attempts and whether they got in.

pythonstats = {
    "attempts": 0,
    "access_granted": False
}

The correct password is "python123". Each wrong guess increments attempts. If they get it right, set access_granted to True and break. Print the stats at the end.

Expected output:

Enter password: hello
Wrong password!
Enter password: abc
Wrong password!
Enter password: python123
Access granted!

--- Stats ---
Attempts used: 3
Access granted: True


Task 3 — HARD MODE: Quiz Game with Full Stats

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