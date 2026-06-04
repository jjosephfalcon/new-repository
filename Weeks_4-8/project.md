## Kemals First Project

Build an AI chatbot that asks the user for their favorite character, and tell the AI chatbot to act as that 
character for the remainder of the conversation until the user types 'quit'. 

After the AI knows your favorite character, ensure it acts and talks like that favorite character for the remainder of the conversation. 

## Tips/Resources
    User an 'input' to get the users favorite character
    Feed it into the API AI provider(Claude/ChatGPT/Gemini)
    
## Example of how to use an AI provider is below, follow this pattern. 

```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5.5",
    input="Explain the concept of quantum computing in one simple sentence."
)
```
