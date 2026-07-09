```markdown
# Task 1 — Look Up + Handle Missing Heroes

Copy this dictionary into your file:

powers = {
    "Spider-Man": "web-slinging",
    "Thor": "lightning",
    "Hulk": "super strength",
    "Iron Man": "powered armor",
    "Black Widow": "combat mastery"
}

Write a while loop that keeps asking the user for a hero name. If the hero is in the dictionary, print their power. If not, print "Hero not found!" Quit when they type "quit".

Expected output:
Enter a hero: Thor
Thor's power is lightning

Enter a hero: Batman
Hero not found!

Enter a hero: quit
Goodbye!

---

# Task 2 — Loop + Count

Use the same dictionary. Loop through every hero and print their name and power. Then print the total number of heroes at the end.

Expected output:
Spider-Man's power is web-slinging
Thor's power is lightning
Hulk's power is super strength
Iron Man's power is powered armor
Black Widow's power is combat mastery

Total heroes: 5

💡 Hint: you don't need to count manually — there's a built-in function for that(find it on google).

---

# Task 3 — Function + Dictionary

Define a function called get_power(hero) that takes a hero name and returns their power. If the hero isn't found, return "Unknown hero!"

Then write a while loop outside the function that asks the user for a hero name, calls get_power(), and prints the result. Quit on "quit".

Expected output:
Enter a hero: Hulk
Hulk's power is super strength

Enter a hero: Deadpool
Unknown hero!

Enter a hero: quit
Goodbye!
```