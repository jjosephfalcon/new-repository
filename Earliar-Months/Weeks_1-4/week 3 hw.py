"""
import random
name = input("Enter the characters name ")
dictionary = {"spiderman": ["shoot webs", "web-shoot","fly w webs"], "superman": ["superpunch","laser eyes","cold breath"], "batman": ["batarang", "acrobatics", "intelligence"]}

def get_power(hero):
    if hero in dictionary:
        return random.choice(dictionary[hero])
    else:
        return "Hero not found"

if name in dictionary:
    print(name, "is in the dictionary and their power is", random.choice(dictionary[name]))
else:
    print(name, "is not in the dictionary")

"""
import random

# Task 1 - Dictionary Lookup
heroes = {
    "Spider-Man": "Shoots webs and wall-crawling",
    "Batman": "Master detective and martial artist",
    "Iron Man": "Genius inventor with a powerful suit",
    "Wonder Woman": "Super strength and Lasso of Truth",
    "Flash": "Super speed"
}

hero_name = input("Enter a hero name: ")

if hero_name in heroes:
    print(f"Power: {heroes[hero_name]}")
else:
    print(f"{hero_name} is not in the database.")


# Task 2 - Multiple Responses with Random
heroes = {
    "Spider-Man": ["Shoots webs and wall-crawling", "Has spider-sense", "Super strength"],
    "Batman": ["Master detective and martial artist", "High-tech gadgets", "Intimidation tactics"],
    "Iron Man": ["Genius inventor with a powerful suit", "Flight capability", "Repulsor beams"],
    "Wonder Woman": ["Super strength and Lasso of Truth", "Indestructible bracelets", "Flight"],
    "Flash": ["Super speed", "Time travel", "Phasing through objects"]
}

def get_power(hero):
    if hero in heroes:
        return random.choice(heroes[hero])
    else:
        return "Hero not found"

hero_name = input("Enter a hero name: ")
print(f"Power: {get_power(hero_name)}")


# Task 3 - Wrap it in a Function
heroes = {
    "Spider-Man": ["Shoots webs and wall-crawling", "Has spider-sense", "Super strength"],
    "Batman": ["Master detective and martial artist", "High-tech gadgets", "Intimidation tactics"],
    "Iron Man": ["Genius inventor with a powerful suit", "Flight capability", "Repulsor beams"],
    "Wonder Woman": ["Super strength and Lasso of Truth", "Indestructible bracelets", "Flight"],
    "Flash": ["Super speed", "Time travel", "Phasing through objects"]
}

def get_power(hero):
    if hero in heroes:
        return random.choice(heroes[hero])
    else:
        return "Hero not found"

hero_name = input("Enter a hero name: ")
result = get_power(hero_name)
print(f"Power: {result}")


# Task 4 - While Loop + Quit
heroes = {
    "Spider-Man": ["Shoots webs and wall-crawling", "Has spider-sense", "Super strength"],
    "Batman": ["Master detective and martial artist", "High-tech gadgets", "Intimidation tactics"],
    "Iron Man": ["Genius inventor with a powerful suit", "Flight capability", "Repulsor beams"],
    "Wonder Woman": ["Super strength and Lasso of Truth", "Indestructible bracelets", "Flight"],
    "Flash": ["Super speed", "Time travel", "Phasing through objects"]
}

def get_power(hero):
    if hero in heroes:
        return random.choice(heroes[hero])
    else:
        return "Hero not found"

while True:
    hero_name = input("Enter a hero name: ")
    if hero_name.lower() == "quit":
        print("Later!")
        break
    result = get_power(hero_name)
    print(f"Power: {result}")
    print()
