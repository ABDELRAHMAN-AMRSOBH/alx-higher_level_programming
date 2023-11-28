#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number > 0:
    x = number % 10
elif number < 0:
    x = (-1 * number) % 10
if x == 0:
    print(f"Last digit of {number:d} is {x:d} and is 0")
elif x > 5 and number > 5:
    print(f"Last digit of {number:d} is {x:d} and is greater than 5")
else:
    print(f"Last digit of {number:d} is {x:d} and is less than 6 and not 0")
