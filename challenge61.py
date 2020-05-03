"""
Implement integer exponentiation. That is, implement the pow(x, y) function, 
where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
"""
import timeit

def trivialPow(num, p):
    res = 1
    for i in range(p):
        res *= num
    return res

def improvedPow(num, p):
    h = p//2
    res = 1
    for i in range(h):
        res *= num
    if p%2 == 0:
        return res*res
    else:
        return res*res*num
    
if __name__ == "__main__":
    s = "trivialPow(2, 20)"
    trivial_time = timeit.timeit(stmt = s, setup="from __main__ import trivialPow")
    s = "improvedPow(2, 20)"
    improved_time = timeit.timeit(stmt = s, setup="from __main__ import improvedPow")
    improvement = round((trivial_time/improved_time)*100) - 100
    print("Time improved for %i perc" % improvement)
