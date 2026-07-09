
"""

import requests





response1 = input("Type 'enter' for a joke or 'quit' to stop: ")

while True:

    response = requests.get("https://official-joke-api.appspot.com/random_joke")

    print(response.text)

    if response1 == "enter":

        print(response)

        break

        input = ("if you want another joke press enter again")

        print(response)

    else:

        response1 == "quit"

"""
import requests



while True:
    response1 = input("Type 'enter' for a joke or 'quit' to stop: ")
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    
    
    if response1 == "quit":
        print("goodbye")
        break
        

    if response.status_code == 200:
           joke_data = response.json()
           print(f"{joke_data['setup']} - {joke_data['punchline']}")
    else:
            print("Couldn't grab a joke right now. Try again!")
        




"""
import requests

while True:
    user_choice = input("Press 'Enter' for a joke or type 'quit' to stop: ").lower()

    if user_choice == "quit":
        print("See ya later!")
        break
    
    # If the user pressed enter (or typed anything else other than quit)
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    
    if response.status_code == 200:
        joke_data = response.json()
        print(f"{joke_data['setup']} - {joke_data['punchline']}")
       
    else:
        print("Couldn't grab a joke right now. Try again!")
"""