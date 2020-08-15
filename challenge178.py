"""Alice wants to join her school's Probability Student Club. Membership dues 
are computed via one of two simple probabilistic games.
    The first game: roll a die repeatedly. Stop rolling once you get a five followed
by a six. Your number of rolls is the amount you pay, in dollars.
    The second game: same, except that the stopping condition is a five followed
by a five.
Which of the two games should Alice elect to play? Does it even matter? 
Write a program to simulate the two games and calculate their expected value."""
import random
import matplotlib.pyplot as plt

#The kind of game the girls chooses does not matter
def die_game(n1, n2):
    rolls = [random.randint(1, 6), random.randint(1, 6)]
    while not (rolls[-2] == n1 and rolls[-1] == n2):
        rolls.append(random.randint(1, 6))
    return len(rolls)

def simulate(n1, n2, times):
    outcomes = []
    for _ in range(times):
        outcomes.append(die_game(n1, n2))
    plt.hist(outcomes)
    return round(sum(outcomes)/len(outcomes), 2)

if __name__ == "__main__":
    print("Expected value of the 1st game: ", simulate(5, 6, 10))
    print("Expected value of the 2nd game: ", simulate(5, 5, 10))
    