## Homework Test Problem

## Task 1 — Restaurant Ordering System
Copy this dictionary into your file:
~~~python
menu = {
    "burger": 8.99,
    "pizza": 11.99,
    "sushi": 14.99,
    "tacos": 7.49,
    "pasta": 10.99
}
~~~
Write a while loop that lets the user order multiple items. Keep a running **total** and a **list** of what they ordered. If the item isn't on the menu, print `"Not on the menu!"` and don't add anything. When they type `"quit"`, print their full order and the total cost.

Expected output:
~~~
Enter a food: pizza
Added pizza ($11.99) to your order.
Enter a food: hotdog
Not on the menu!
Enter a food: tacos
Added tacos ($7.49) to your order.
Enter a food: quit
Your order: pizza, tacos
Total: $19.48
Goodbye!
~~~
💡 Hints:
- Use a list to track ordered items and a float variable for the total.
- Use `round(total, 2)` when printing so you don't get floating point weirdness.
---