
# Homework 5 — Joseph
New file: chatbot.py

## Task 1 — Install OpenAI

Open your terminal and run:

pip install openai

Then add your OpenAI API key to your .env file:


OPENAI_API_KEY=your_key_here

## Task 2 — Basic Completion

In chatbot.py, load your API key from .env and send a hardcoded message to the OpenAI API. Print the response.

Example output:

Believe it! I never give up no matter what!


## Task 3 — User Input

Ask the user what they want to say, pass it to the API, and print the response.

Example output:

What do you want to say? What's your strongest move?

Naruto says: My Rasengan is unstoppable!

## Task 4 — Add a System Prompt + While Loop

Tell the API to respond as your chosen character using a system prompt. Wrap everything in a while loop so the conversation keeps going until the user types "quit".

Example output:

What do you want to talk about? Fighting

Naruto says: Believe it! I never back down from a fight!

What do you want to talk about? quit

Goodbye!

# Resources

https://developers.openai.com/api/reference/python