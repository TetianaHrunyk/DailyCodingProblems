"""You are given a starting state start, a list of transition probabilities 
for a Markov chain, and a number of steps num_steps. Run the Markov 
chain starting from start for num_steps and compute the number of times we 
visited each state.
For example, given the starting state a, number of steps 5000, and the following 
transition probabilities:
[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
One instance of running this Markov chain might produce 
{ 'a': 3012, 'b': 1656, 'c': 332 }"""
import random

class MarkovChain:
    
    def __init__(self, states):
        self.visited = dict()   
        self.states = dict()
        unique_states = []
        for state in states:
            if state[0] not in unique_states:
                unique_states.append(state[0])
        self.unique_states = unique_states
        for state in unique_states:
            cur = [s for s in states if s[0]==state]
            cur = sorted(cur, key=lambda x: x[-1])
            val = dict()
            val[cur[0][1]] = [0, cur[0][2]]
            for c in range(1, len(cur)):
                val[cur[c][1]] = [val[cur[c-1][1]][1], val[cur[c-1][1]][1]+cur[c][2]]
            self.states[state] = val     
        
        
    def run_once(self, in_state):
        p = random.random()
        states = self.states[in_state]
        for state, interval in states.items():
            if p >= interval[0] and p < interval[1]:
                return state
        
    def run_n_times(self, n, in_state):
        res = dict()
        for state in self.unique_states:
            res[state] = 0
        for _ in range(n):
            new_in = self.run_once(in_state)
            res[new_in] += 1
            in_state = new_in
        return res
        
        
if __name__ == "__main__":
    chain = MarkovChain([
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
])
    print(chain.run_n_times(5000, 'a'))
    
    
    
    
    
    