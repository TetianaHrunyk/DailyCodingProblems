"""Given an integer n and a list of integers l, write a function that randomly 
generates a number from 0 to n-1 that isn't in l (uniform).
"""
import random

def randomLessThanN(n: int, l: list):
    l.append(n)
    l.sort()
    nums_in_l = set(l[:l.index(n)])
    nums_less_than_n = set(i for i in range(n))
    options = list(nums_less_than_n - nums_in_l)
    if len(options) > 0:
        return random.choice(options)
    else:
        return None
    
if __name__ == "__main__":
    l = []
    for i in range(20):
        l.append(random.randint(1, 40))
    print(l)
    print(randomLessThanN(8, l))
    