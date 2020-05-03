"""
Given a function that generates perfectly random numbers between 1 and k 
(inclusive), where k is an input, write a function that shuffles 
a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
"""
import random
import matplotlib.pyplot as plt

def shuffle(deck: list)->list:
    size = len(deck)
    for i in range(size^2):
        a, b = random.randint(0, size-1), random.randint(0, size-1)
        deck[a], deck[b] = deck[b], deck[a]
    return deck

def avgDistanceAfterSfuffling(before, after):
    distances = []
    for i in range(len(before)):
        distance = abs(i - after.index(before[i]))
        distances.append(distance)
    return sum(distances)/len(before)

if __name__ == "__main__":
    deck = ["A", "B", "C", "D", "E", "F", "G", "H", "Y", "Z", "L", "M", "N", "O", "P", "Q"]
    
    avg_distances = [avgDistanceAfterSfuffling(deck, shuffle(deck.copy())) for i in range(100)]
    plt.hist(avg_distances, bins = 10)
    plt.xlabel("Number of occurances")
    plt.ylabel("Avg Distance")