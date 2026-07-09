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

## July 3rd Feedback

 
Build an AI chatbot that asks the user for their favorite character, and tell the AI chatbot to act as that character for the remainder of the conversation until the user types 'quit'.
 
After the AI knows your favorite character, ensure it acts and talks like that favorite character for the remainder of the conversation.
 
Tips/Resources

User an 'input' to get the users favorite character

Feed it into the API AI provider(Claude/ChatGPT/Gemini)

Example of how to use an AI provider is below, follow this pattern.

from openai import OpenAI
 
client = OpenAI()
 
response = client.responses.create(
    model="gpt-5.5",
    input="Explain the concept of quantum computing in one simple sentence."
)