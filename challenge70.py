"""
A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
"""

def nth_perfect_number(n):
    n_digit_sum = 0
    n_str = str(n)
    for i in n_str:
        n_digit_sum += int(i)
        
    return (n * 10) + (10 - n_digit_sum)
    
if __name__ == "__main__":
    assert nth_perfect_number(1) == 19
    assert nth_perfect_number(2) == 28
    assert nth_perfect_number(51) == 514
    assert nth_perfect_number(19) == 190