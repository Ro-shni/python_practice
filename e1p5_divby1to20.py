'''
from math import gcd
from functools import reduce

def lcm(a, b):
    return (a * b) // gcd(a, b)

n = 1
for i in range(2, 21):
    n = lcm(n, i)

print(n)''' #most effective solution


n = 20
while True:
    is_divisible = True
    for i in range(1, 21):
        if n % i != 0:
            is_divisible = False
            break
    if is_divisible:
        print(n)
        break
    n += 20


