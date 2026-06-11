# Eshwars Example for the AI project

import os
from openai import OpenAI


client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

character = input("What is your favorite cartoon character? ")

while True:

    userInput = input("Enter input for AI")
    if character == "quit":
        break

    response = client.responses.create(
        model="gpt-5.5",
        instructions=f"Your task is to act like the cartoon character {character} and respond like him",
        input= userInput,
    )

    print(response.output_text)



# Task 1 — Country Capitals

### Step 1: Create a dictionary called capitals that stores at least 5 countries and their capital cities.

### Step 2: Define a function called get_capital(country) that takes a country name and returns the capital. If the country isn't in the dictionary, return "I don't know that one!".

💡 Hint: use .get() on your dictionary or check with in.

### Step 3: Write a while loop that asks the user to enter a country. If they type "quit", print "Goodbye!" and break. Otherwise, call get_capital() and print the result.

Expected output:
Enter a country (or quit): France
Paris

Enter a country (or quit): Japan
Tokyo

Enter a country (or quit): Narnia
I don't know that one!

Enter a country (or quit): quit
Goodbye!

# Task 2 Cheat Code Checker

### Step 1
Create a dictionary called cheat_codes where the keys are codes (strings) and the values are what they unlock.

Example:

pythoncheat_codes = {
    "IDDQD": "God mode activated!",
    "BIGHEAD": "Big head mode on!",
    "NOCLIP": "Walk through walls enabled!"
}

### Step 2: 

Define a function called check_code(code) that looks up the code in the dictionary and returns what it unlocks. If the code isn't valid, return "Invalid code.".

### Step 3

Write a while loop that asks the user to enter a cheat code. If they type "quit", print "Goodbye!" and break. Otherwise, call check_code() and print the result.

Expected output:
Enter a cheat code (or quit): IDDQD
God mode activated!

Enter a cheat code (or quit): BIGHEAD
Big head mode on!

Enter a cheat code (or quit): BANANA
Invalid code.

Enter a cheat code (or quit): quit
Goodbye!


Task 2 — Cheat Code Checker
Step 1: Create a dictionary called cheat_codes where the keys are codes (strings) and the values are what they unlock.
Example:
pythoncheat_codes = {
    "IDDQD": "God mode activated!",
    "BIGHEAD": "Big head mode on!",
    "NOCLIP": "Walk through walls enabled!"
}
Step 2: Define a function called check_code(code) that looks up the code in the dictionary and returns what it unlocks. If the code isn't valid, return "Invalid code.".
Step 3: Write a while loop that asks the user to enter a cheat code. If they type "quit", print "Goodbye!" and break. Otherwise, call check_code() and print the result.
Expected output:
Enter a cheat code (or quit): IDDQD
God mode activated!

Enter a cheat code (or quit): BIGHEAD
Big head mode on!

Enter a cheat code (or quit): BANANA
Invalid code.

Enter a cheat code (or quit): quit
Goodbye!

Task 3 — Positive or Negative
Step 1: Define a function called check_sign(num) that takes a number and returns:

"Positive" if it's above 0
"Negative" if it's below 0
"Zero" if it's exactly 0

Step 2: Write a while loop that asks the user to enter a number. If they type "quit", print "Goodbye!" and break. Otherwise, convert to an integer, call check_sign(), and print the result.
Expected output:
Enter a number (or quit): 10
Positive

Enter a number (or quit): -4
Negative

Enter a number (or quit): 0
Zero

Enter a number (or quit): quit
Goodbye!
