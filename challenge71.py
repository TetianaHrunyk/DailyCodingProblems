"""
Using a function rand7() that returns an integer from 1 to 7 (inclusive) with
 uniform probability, implement a function rand5() that returns an integer
 from 1 to 5 (inclusive).
"""

import random
import matplotlib.pyplot as plt

def rand7():
    return random.randint(1, 7)

def rand5():
    num = rand7()
    while num > 5:
        num = rand7()
    return num

if __name__ == "__main__":
    outcomes = [rand5() for i in range(10000)]
    plt.hist(outcomes, bins = 5)