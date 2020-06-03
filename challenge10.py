"""Implement a job scheduler which takes in a function f and an integer n, 
and calls f after n milliseconds.
"""

import time

def scheduler(n, f):
    time.sleep(n/100)
    return f()

f = lambda : print("Function was run")

scheduler(10, f)
