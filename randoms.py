# A python program that generate a random set of numbers between 1 and ten.
# Use set operations to remove duplicates and display the unique numbers.

import random, args

numbers = []
total = 0

for _ in range(1, 10):
    numbers.append(random.randint(1, 10))

num_set = set(numbers)

for num in num_set:
    total += args.add(num)

print(f"{num_set} with a total of {total}.")
