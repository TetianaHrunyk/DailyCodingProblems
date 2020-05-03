"""
This problem was asked by Google.

The power set of a set is the set of all its subsets.
 Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3},
 it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
"""
import math

def powerSubset(s: list) -> set:
    start, end = 0, 0
    res = []
    for i in range(len(s)):
        for j in range(len(s)-start):
            res.append([start:end])
        