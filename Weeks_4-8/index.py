#Write a function called `is_even(number)` that returns `True` if the number is even and `False` if it's odd.

def is_even(number):
    
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


print(is_even(20))