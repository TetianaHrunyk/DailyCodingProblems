"""Given an even number (greater than 2), return two prime numbers whose sum
 will be equal to the given number.
A solution will always exist. See Goldbach’s conjecture.
Example:
Input: 4
Output: 2 + 2 = 4
If there are more than one solution possible, return the lexicographically smaller 
solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then
[a, b] < [c, d]
If a < c OR a==c AND b < d."""

def is_prime(num):
    for i in range(2, num//2):
        if num%i == 0:
            return False
    return True
    
    
def prime_sum(num):
    for i in range(2, num):
        if is_prime(i):
            candidate = num - i
            if is_prime(candidate):
                return (i, candidate)
    return None

if __name__ == "__main__":
    assert prime_sum(4) == (2, 2)
    assert prime_sum(10) == (3, 7)
    assert prime_sum(169) == (2, 167)