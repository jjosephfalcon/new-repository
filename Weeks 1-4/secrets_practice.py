import os
example_secret_word = os.environ.get("SECRET_WORD")
print(f"The secret word is: {example_secret_word}")

city = input("enter a city to get the weather: ")
if city.lower() == "new york":
    print(example_secret_word) 
