"""
Using a function rand5() that returns an integer from 1 to 5 (inclusive) 
with uniform probability, 
implement a function rand7() that returns an integer from 1 to 7 (inclusive).
"""
import random
import matplotlib.pyplot as plt


def rand5():
    return random.randint(1, 5)

def rand7():
    #probability of getting 6 or 7
    p = random.random()*100
    #print(p)
    
    if p <= 28.57:
        return random.randint(6, 7)
    else:
        return rand5()
    
if __name__ == "__main__":
    outcomes = [rand7() for i in range(10000)]
    plt.hist(outcomes, bins = 7)
