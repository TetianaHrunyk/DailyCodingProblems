"""You have n fair coins and you flip them all at the same time. Any that come up tails
 you set aside. The ones that come up heads you flip again. How many rounds do you 
 expect to play before only one coin remains?

Write a function that, given n, returns the number of rounds you'd expect to play 
until one coin remains.
"""
import random

#This implementation incorporates randomness and is more probabilistic model
#An alternative, more rigid, implementation would be 
#to simply return math.ceil(math.log2(n))
def expected_plays(n):
    plays = 0
    while n > 0:
        flips = [random.randint(0, 1) for _ in range(n)]
        n -= sum(flips)
        plays += 1
    return plays    
    
if __name__ == "__main__":
    print(expected_plays(4))
    print(expected_plays(10))