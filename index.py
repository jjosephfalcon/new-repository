print("hello world")
name = input("whats your name?")
character = input("whats your fav character?")
print(f"Nice to meet you, {name}! get ready to talk to {character}.")
topic = input("what do you want to talk to them about?")

print(f"Great! {topic} is a great topic to talk to about {name}.")
print(f"{character} says: {topic} is one of my favorite topics to talk about too!")
if topic.lower() == "fighting":
    character_response = "I love fighting! It's so exciting and adrenaline-pumping!"
    print(character_response)
elif topic.lower() == "cooking":    
    character_response = "Cooking is one of my favorite hobbies! I love trying out new recipes and experimenting with different flavors."
    print(character_response) 
elif topic.lower() == "traveling":
    character_response = "Traveling is amazing! I love exploring new places and experiencing different cultures."
    print(character_response)
else:
    character_response = f"{topic} is an interesting topic! I enjoy talking about it too."
    print(character_response)
    #just a change
