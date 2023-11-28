#!/usr/bin/python3
import random
number = random.randint(-15, 15)
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
