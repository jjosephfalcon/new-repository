# Homework 4 — Functions

## Task 1 

Functions are reusable blocks of code. Master these and everything else gets easier.

```
Check this code out:
a = 1
b = 2
print(a + b)
```
That outputs 5 right?

How would you make it easiar so that it is a function that holds and calls the logic?

Create a new file in your Weeks_4-8 folder called functions.py, this is where you will complete Tasks 2-4

For task 2:

Write a function called add that adds two numbers and prints the result.

Calling the add function should look like:

add(a, b)

Should return the addition of whats in the parameters

## Task 2

Write a function called `multiply(a, b)` that returns the product of two numbers.

## Task 3

Write a function called `is_even(number)` that returns `True` if the number is even and `False` if it's odd.

## Task 4 — Countdown Machine

Write a function called countdown(n) that uses a while loop to count down from n to 0 and prints each number.
Expected output:
countdown(5)

5
4
3
2
1
Blast off!

## Task 5 — Guess the Number

Write a function called check_guess(guess, secret) that returns "Too low", "Too high", or "Correct!" depending on the guess.
Then outside the function, write a while loop that keeps asking the user to guess until they get it right.

Expected output:

Guess the number: 3

Too low

Guess the number: 8

Too high

Guess the number: 5

Correct!