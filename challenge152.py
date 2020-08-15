"""You are given n numbers as well as n probabilities that sum up to 1.
Write a function to generate one of the numbers with its corresponding probability.
For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2],
your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20%
of the time.
You can generate random numbers between 0 and 1 uniformly."""
import random
import matplotlib.pyplot as plt

class RandNums:
    
    def __init__(self, nums, probs):
        cum_probs = [0]+[sum(probs[:i+1]) for i in range(len(probs))]
        self.prob_ranges = [(cum_probs[i], cum_probs[i+1]) for i in range(len(cum_probs)-1)]
        self.nums = nums
        
    def get_num(self):
        rand = random.random()
        for i in range(len(self.prob_ranges)):
            r = self.prob_ranges[i]
            if rand >= r[0] and rand < r[1]:
                return self.nums[i]
            
def test(n, nums, probs):
    outcomes = [rnum.get_num() for _ in range(n)]   
    stochastic_probs = [outcomes.count(elem)/n for elem in nums]
    for i in range(len(nums)):
        print(f"Expected probability for {nums[i]}: {probs[i]}; actual: {stochastic_probs[i]}")
    #plt.bar([str(num) for num in nums], stochastic_probs)
    
             
            
if __name__ == "__main__":
    rnum = RandNums([1, 2, 3, 4], [0.1, 0.5, 0.2, 0.2])
    
    test(100, [1, 2, 3, 4], [0.1, 0.5, 0.2, 0.2])
    
    