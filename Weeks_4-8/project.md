## Kemals AI Project

FAILS IMMEDIATELY IF FILE IS MORE THAN 60 LINES
Make the AI conversation continuous, so the chatbot remembers the conversation. 

Read these docs:

https://developers.openai.com/api/docs/guides/conversation-state

To understand how to make it a continuos conversation. 

Key points to understand, the AIs output is always the last message of what was appended in the array

If the array is

"
messages = [
    {"role": "system", "content": "You are Goku."},
    {"role": "user", "content": "hey"},
    {"role": "assistant", "content": "Hey there, what's up?"},
    {"role": "user", "content": "how are you"}
]
"

Then the AI will respond with... The answer to "How are you?" Except it'll have all of the conversation history of the first three messages as well.

## June 29th Feedback

The project solution that you had became a lot more complicated than it needs to be using things like "with open" Creating and reading files when that was not part of the assignment.

The answer to this project should be very simple: less than 40 lines. It doesn't even need to use any functions. It does not need to be more complicated using external libraries

The whole answer should not be more than 35 lines of code. Here is a guide on how to make sure that messages history is Added to the project so the AI has conversation history.

How the Messages List Works

The AI has no memory. Every time you send it a message, it completely forgets everything that happened before — unless you send it the full conversation history yourself.

That's what the messages list is for. It stores every message in the conversation — yours AND the AI's — so you can send the whole thing every time.


What Does One Message Look Like?

Each message is a dictionary with two keys: role and content.

python{"role": "user", "content": "What's your favorite food?"}

The role tells the AI who is talking. There are three options:


system — sets the rules (e.g. "You are SpongeBob")
user — you, the person typing
assistant — the AI's response

A Full Example

Here's what the list looks like after 2 back-and-forth messages:

pythonmessages = [
    {"role": "system",    "content": "You are SpongeBob. Stay in character."},
    {"role": "user",      "content": "What's your favorite food?"},
    {"role": "assistant", "content": "Krabby Patties, duh! ahahahaha!"},
    {"role": "user",      "content": "Do you like Patrick?"},
    {"role": "assistant", "content": "Patrick is my best friend in the whole ocean!"}
]

Every time you send this full list to the AI, it reads the entire conversation from top to bottom and uses it to write the next reply.


How It Grows During the Loop

After every message, two things happen:

Step 1 — append your message:

pythonmessages.append({"role": "user", "content": user_input})

Step 2 — append the AI's reply:

pythonmessages.append({"role": "assistant", "content": reply})

Then the next time you call the API, you pass in the whole updated list.


Why Not Just Send the Last Message?

The AI will act like it's meeting you for the first time every single reply. No memory. No continuity. Sending the full list every time is what makes it feel like a real conversation.


Quick Reference

python# Start the list
messages = [{"role": "system", "content": f"You are {character}."}]

### Add your message

messages.append({"role": "user", "content": user_input})

### Add the AI reply

messages.append({"role": "assistant", "content": reply})

### Send the whole list every time

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages
)