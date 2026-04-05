print("hello world!")
name = input("whats your name? ")
character = input("whats your fav character? ")
age = input("how old are you? ")
print(f"Nice to meet you, {name}! You are {age} years old.")
print(f"Get ready to talk to {character}!")
topic = input("what do you want to talk to them about? ")

print(f"Great! {topic} is a great topic to talk to {character} about.")
print(f"{character} says: {topic} is one of my favorite topics!")
if topic.lower() == "fighting":
    character_response = "I love fighting! It's so exciting and adrenaline-pumping!"
    print(character_response)
elif topic.lower() == "cooking":
    character_response = "Cooking is one of my favorite hobbies! I love trying new recipes."
    print(character_response)
elif topic.lower() == "traveling":
    character_response = "Traveling is amazing! I love exploring new places and cultures."
    print(character_response)
elif topic.lower() == "music":
    character_response = "Music is life! I could listen to it all day long."
    print(character_response)
elif topic.lower() == "gaming":
    character_response = "Gaming is so fun! What's your favorite game?"
    print(character_response)
else:
    character_response = f"{topic} is an interesting topic! I enjoy talking about it too."
    print(character_response)

print(f"Thanks for chatting, {name}! Come back soon.")
