import random
from decimal import *

getcontext().prec = 25
n = 10
jumps = []
sample_size = 100000000

for x in range(sample_size):
    position = 0
    jump = 0
    while position != n:
        jump += 1
        position = random.randint(position + 1, n)
    jumps.append(jump)

# print(str(jumps) + "\n")

print(Decimal(sum(jumps)/len(jumps)))

print(max(jumps))