"""
a = 1
b = 2
def add(a,b):
    return a + b
print(add(a,b))

    
def add(a, b):
    print(a + b)
    return a + b


def multiply(a, b):
    return a * b

def is_even(number):
    return number % 2 == 0


def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    return "Blast off"
print(countdown(5)) 


def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Blast off!")

countdown(5)


secret = 4

def check_guess(guess, secret):
    if guess == secret:
        return "Correct!"
    elif guess < secret:
        return "too low"
    else:
        return "too high"
    check_guess(guess,secret)


while True: 
    guess = int(input("Guess the number: "))
    print(check_guess(guess,secret))
    if guess == "too low" or "too high":
      break
"""

## Task 1 — Your First Function

# Step 1: Define a function called `greet` that takes one parameter called `name`.

# Step 2: Inside the function, return a greeting string that includes the name.

# Step 3: Outside the function, call `greet` with your name and print the result.

# # Expected output:

# ```
# Hello, Kemal!
# ```

# ---
"""
name = ""
def greet(name):
    return f"Hello, {name}"
print(greet("Kemal"))
"""

# Step 1: Define a function called `check_even` that takes one parameter called `number`.

# Step 2: Inside the function, use an if/else to check if the number is even or odd. (Hint: use %)

# Step 3: Return "Even!" or "Odd!" depending on the result.

# Step 4: Outside the function, call `check_even` with a few different numbers and print each result.

# Expected output:

# ```
"""
def check_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
for number in [4,6,9,10]:
    print(check_even(number))
"""

# Step 1: Define a function called say_hello that takes one parameter called name and returns a greeting with the name in it.

# Step 2: Outside the function, write a while loop that asks the user to enter a name.

# Step 3: Inside the while loop, call say_hello with what the user typed and print the result.

# Step 4: If the user types "quit", print "Goodbye!" and break out of the loop.
"""
def say_hello(name):
    return f"hello, {name}!"

while True:
    name = input("enter a name: ")
    if name == "quit":
        print("Goodbye!")
        break
    print(say_hello(name))
"""
## Task 4 — Function with If/Else Inside a While Loop

# Step 1: Define a function called `check_password` that takes one parameter called `password`.

# Step 2: Inside the function, check if the password equals "python123". Return "Access granted!" if it does, "Wrong password!" if it doesn't.

# Step 3: Outside the function, write a while loop that asks the user to enter a password.

# Step 4: Inside the while loop, call `check_password` with what the user typed and print the result.

# Step 5: If the result is "Access granted!", break out of the loop.
"""
def check_password(password):
    if password == "python123":
        return "Access granted!"
    else:
        return "Wrong password!"

while True:
    password = input("What is the password? ")
    result = check_password(password)
    print(result)
    if result == "Access granted!":
        break
"""
## Task 5 — Guess the Number

# Write a function called check_guess(guess, secret) that returns "Too low", "Too high", or "Correct!" depending on the guess.
# Then outside the function, write a while loop that keeps asking the user to guess until they get it right.

# Expected output:

# Guess the number: 3

# Too low

# Guess the number: 8

# Too high

# Guess the number: 5

# Correct!
# secret = "5"
# guess = input("what is the number")
# def check_guess(guess, secret):
#     if guess > "5": 
#      return "too high"
#     elif guess < "5":
#        return "too low"
#     if guess == "5":
#        return "correct"
# print(check_guess(guess, 5))
secret = 5
def check_guess(guess, secret):
    if guess > secret:
        return "Too high"
    elif guess < secret:
        return "Too low"
    else:
        return "Correct!"

while True:
    guess = int(input("Guess the number: "))
    result = check_guess(guess, secret)
    print(result)
    if result == "Correct!":
        break