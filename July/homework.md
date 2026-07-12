# Homework — Dictionaries + Functions + While Loops

## Task 1 — Restaurant Menu

Copy this dictionary into your file:

```
menu = {
    "burger": 8.99,
    "pizza": 11.99,
    "sushi": 14.99,
    "tacos": 7.49,
    "pasta": 10.99
}
```

Write a while loop that asks the user for a food item. If it's in the menu, print the price. If not, print `"Not on the menu!"` Quit when they type `"quit"`.

Expected output:
```
Enter a food: pizza
pizza costs $11.99

Enter a food: hotdog
Not on the menu!

Enter a food: quit
Goodbye!
```

---

## Task 2 — Country Capitals

Copy this dictionary into your file:

```
capitals = {
    "Japan": "Tokyo",
    "France": "Paris",
    "Brazil": "Brasilia",
    "Kenya": "Nairobi",
    "Canada": "Ottawa"
}
```

Write a function called `get_capital(country)` that takes a country name and returns its capital. If the country isn't found, return `"Country not found!"`.

Then write a while loop that asks the user for a country, calls `get_capital()`, and prints the result. Quit on `"quit"`.

Expected output:
```
Enter a country: Japan
The capital of Japan is Tokyo

Enter a country: Australia
Country not found!

Enter a country: quit
Goodbye!
```

---

## Task 3 — Sports + Counting

Copy this dictionary into your file:

```
sports = {
    "LeBron": "basketball",
    "Messi": "soccer",
    "Serena": "tennis",
    "Usain": "sprinting",
    "Federer": "tennis"
}
```

Write a function called `get_sport(athlete)` that returns their sport or `"Athlete not found!"` if they're not in the dictionary.

Write a while loop that asks for an athlete name, calls `get_sport()`, and prints the result. Keep count of how many athletes were found successfully. Print the total when they quit.

Expected output:
```
Enter an athlete: Messi
Messi plays soccer

Enter an athlete: Jordan
Athlete not found!

Enter an athlete: Serena
Serena plays tennis

Enter an athlete: quit
You looked up 2 athletes.
Goodbye!
```

💡 Hint: only add to the count if the athlete was actually found.