## Task 1 — Grade Checker

**Step 1:** Define a function called `check_grade(score)` that takes one parameter called `score`.

**Step 2:** Inside the function, check the score and return the matching grade:
- 90 or above → return `"A"`
- 80–89 → return `"B"`
- 70–79 → return `"C"`
- Below 70 → return `"F"`

**Step 3:** Outside the function, write a while loop that asks the user to enter a score.

**Step 4:** If the user types `"quit"`, print `"Goodbye!"` and break out of the loop. Otherwise, call `check_grade()` with the score and print the result.

**Expected output:**
```
Enter a score (or quit): 95
A

Enter a score (or quit): 82
B

Enter a score (or quit): 71
C

Enter a score (or quit): 55
F

Enter a score (or quit): quit
Goodbye!
```

---

## Task 2 — Even or Odd

**Step 1:** Define a function called `check_number(num)` that takes one parameter called `num`.

**Step 2:** Inside the function, check if the number is even or odd and return the result:
- Even → return `"Even"`
- Odd → return `"Odd"`

**Step 3:** Outside the function, write a while loop that asks the user to enter a number.

**Step 4:** If the user types `"quit"`, print `"Goodbye!"` and break. Otherwise, convert the input to an integer and call `check_number()`, then print the result.

> 💡 Hint: use `int()` to convert the user's input to a number before passing it into the function.

**Expected output:**
```
Enter a number (or quit): 4
Even

Enter a number (or quit): 7
Odd

Enter a number (or quit): 100
Even

Enter a number (or quit): quit
Goodbye!
```

---

## Task 3 — Temperature Mood

**Step 1:** Define a function called `check_temp(temp)` that takes one parameter called `temp`.

**Step 2:** Inside the function, check the temperature and return the matching mood:
- Below 32 → return `"Freezing!"`
- 32–70 → return `"Pretty cold."`
- Above 70 → return `"Nice out!"`

**Step 3:** Outside the function, write a while loop that asks the user to enter a temperature.

**Step 4:** If the user types `"quit"`, print `"Goodbye!"` and break. Otherwise, call `check_temp()` with the temperature and print the result.

**Expected output:**
```
Enter a temperature (or quit): 20
Freezing!

Enter a temperature (or quit): 55
Pretty cold.

Enter a temperature (or quit): 85
Nice out!

Enter a temperature (or quit): quit
Goodbye!
```