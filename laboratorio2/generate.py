import random

# generate 5000000 random numbers
with open("data.txt", 'w') as f:
  for i in range(1, 500001):
    f.write(f"{random.random()}\n")