## IMPORTANT - watch this video on functions

https://www.youtube.com/watch?v=u-OmVr_fT4s

This video will be helpful for you to clear up any gaps on functions. 

https://www.youtube.com/watch?v=rRTjPnVooxE

This video will be helpful for you to clear up any gaps on while loops. 

## Task 1 — Your First Function

Step 1: Define a function called `greet` that takes one parameter called `name`.

Step 2: Inside the function, return a greeting string that includes the name.

Step 3: Outside the function, call `greet` with your name and print the result.

Expected output:

```
Hello, Kemal!
```

---

## Task 2 — Function + If/Else

Step 1: Define a function called `check_even` that takes one parameter called `number`.

Step 2: Inside the function, use an if/else to check if the number is even or odd. (Hint: use %)

Step 3: Return "Even!" or "Odd!" depending on the result.

Step 4: Outside the function, call `check_even` with a few different numbers and print each result.

Expected output:

```
Even!

Odd!
```

---

## Task 3 — Function Inside a While Loop

Step 1: Define a function called `say_hello` that takes one parameter called `name` and returns a greeting with the name in it.

Step 2: Outside the function, write a while loop that asks the user to enter a name.

Step 3: Inside the while loop, call `say_hello` with what the user typed and print the result.

Step 4: If the user types "quit", print "Goodbye!" and break out of the loop.

Expected output:

```
Enter a name: Kemal

Hello, Kemal!

Enter a name: quit

Goodbye!
```

---

## Task 4 — Function with If/Else Inside a While Loop

Step 1: Define a function called `check_password` that takes one parameter called `password`.

Step 2: Inside the function, check if the password equals "python123". Return "Access granted!" if it does, "Wrong password!" if it doesn't.

Step 3: Outside the function, write a while loop that asks the user to enter a password.

Step 4: Inside the while loop, call `check_password` with what the user typed and print the result.

Step 5: If the result is "Access granted!", break out of the loop.

Expected output:

```
Enter password: hello

Wrong password!

Enter password: python123

Access granted!
```

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