"""
Assume you have access to a function toss_biased() which returns 0 or 1 with
 a probability that's not 50-50 (but also not 0-100 or 100-0).
 You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.
"""

import random
BIAS = 0.2

def toss_biased():
    if random.random() >= (0.5+BIAS):
        return 1
    else:
        return 0
    
def unbiased_toss():
    toss = toss_biased()
    if toss:
        return toss
    else:
        return toss_biased() 

if __name__ == "__main__":
    tosses = [unbiased_toss() for _ in range(1000)]
    m = sum(tosses)/len(tosses)
    print("Mean value: ", round(m, 2))