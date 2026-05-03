# import random

# # Task 1 - Dictionary Lookup
# heroes = {
#     "Spider-Man": "Shoots webs and wall-crawling",
#     "Batman": "Master detective and martial artist",
#     "Iron Man": "Genius inventor with a powerful suit",
#     "Wonder Woman": "Super strength and Lasso of Truth",
#     "Flash": "Super speed"
# }

# hero_name = input("Enter a hero name: ")

# if hero_name in heroes:
#     print(f"Power: {heroes[hero_name]}")
# else:
#     print(f"{hero_name} is not in the database.")


# # Task 2 - Multiple Responses with Random
# heroes = {
#     "Spider-Man": ["Shoots webs and wall-crawling", "Has spider-sense", "Super strength"],
#     "Batman": ["Master detective and martial artist", "High-tech gadgets", "Intimidation tactics"],
#     "Iron Man": ["Genius inventor with a powerful suit", "Flight capability", "Repulsor beams"],
#     "Wonder Woman": ["Super strength and Lasso of Truth", "Indestructible bracelets", "Flight"],
#     "Flash": ["Super speed", "Time travel", "Phasing through objects"]
# }

# import random

# heroes = {
#     "Spider-Man": ["Shoots webs and wall-crawling", "Has spider-sense", "Super strength"],
#     "Batman": ["Master detective and martial artist", "High-tech gadgets", "Intimidation tactics"],
#     "Iron Man": ["Genius inventor with a powerful suit", "Flight capability", "Repulsor beams"],
#     "Wonder Woman": ["Super strength and Lasso of Truth", "Indestructible bracelets", "Flight"],
#     "Flash": ["Super speed", "Time travel", "Phasing through objects"]
# }


    
# #Write your function here

# def get_power(hero):
#     if hero in heroes:
#         return random.choice(heroes[hero])
#     else:
#         return f"{hero} is not in the database"

# #Final ouput
# hero_name = input("Enter a hero name: ")
# #hero_name = Batman
# print(f"Power: {get_power(hero_name)}")


numbers = [1, 2, 3, 4, 5]

def pick_number(index):
    return numbers[index] 

print(pick_number(3))

