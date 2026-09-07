# 🏀 NBA Player Lookup — In-Class Problem

## Setup — Use This Dictionary (Already Given)

```python
players = {
    "LeBron": {"team": "Lakers", "ppg": 25.7},
    "Curry": {"team": "Warriors", "ppg": 29.4},
    "KD": {"team": "Suns", "ppg": 27.1},
    "Giannis": {"team": "Bucks", "ppg": 30.4},
    "Luka": {"team": "Mavericks", "ppg": 33.9}
}
```

## Task 1 — Write the Function
Define a function called `get_player(name)` that looks up the player in the dictionary.
- If found, return a formatted string with their team and PPG.
- If not found, return `"Player not found!"`

## Task 2 — Write the While Loop
Write a while loop that:
- Asks the user to enter a player name
- Calls `get_player()` and prints the result
- If the user types `"quit"`, print `"Goodbye!"` and break

## Expected Output
```
Enter a player (or quit): LeBron
Team: Lakers | PPG: 25.7

Enter a player (or quit): Jordan
Player not found!

Enter a player (or quit): quit
Goodbye!
```

💡 **Hint:** The dictionary is nested — to get the team, you can't just do `players[name]`. Think about what that gives you first.