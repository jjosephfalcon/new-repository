def check_guess(guess, secret):
    if guess < secret:
        return "Too low"
    elif guess > secret:
        return "Too high"
    else:
        return "Correct!"

secret = 5

while True:
    guess = int(input("Guess the number: "))
    result = check_guess(guess, secret)
    print(result)
    if result == "Correct!":
        break
















