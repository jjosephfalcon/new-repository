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
