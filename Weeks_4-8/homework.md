Task 1 — Football Players

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

Task 2 — Password Checker with Dictionary

The user gets 3 attempts to guess the correct password. Track attempts and whether they got in.

stats = {
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
