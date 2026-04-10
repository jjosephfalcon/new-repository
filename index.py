characters = ["naruto", "goku", "luffy", "eren", "tanjiro"]

print("hello world!")
name = input("whats your name? ")

# Show available characters
print("Available characters:", characters)
character = input("whats your fav character? ")

# Validate character choice
if character.lower() not in characters:
    print("Error: That character is not available. Goodbye!")
    quit()

age = input("how old are you? ")
print(f"Nice to meet you, {name}! You are {age} years old.")
print(f"Get ready to talk to {character}!")

# Task 4 — Dictionary instead of if/elif
responses = {
    "fighting": "I love fighting! It's so exciting and adrenaline-pumping!",
    "cooking": "Cooking is one of my favorite hobbies! I love trying new recipes.",
    "traveling": "Traveling is amazing! I love exploring new places and cultures.",
    "music": "Music is life! I could listen to it all day long.",
    "gaming": "Gaming is so fun! What's your favorite game?"
}