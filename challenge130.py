"""Given an array of numbers representing the stock prices of a company in chronological
 order and an integer k, return the maximum profit you can make from k buys and sells. 
 You must buy the stock before you can sell it, and you must sell the stock before 
 you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3."""

def max_profit(prices, cur_prof, k):
    if k == 0 or len(prices) <= 1:
        return cur_prof
    return max(max_profit(prices[2:], cur_prof + (prices[1]-prices[0]), k-1), max_profit(prices[1:], cur_prof, k))


if __name__ == "__main__":
    assert max_profit([5, 2, 4, 0, 1], 0, 2) == 3
    assert max_profit([5, 2, 4], 0, 2) == 2
    assert max_profit([5, 2, 4], 0, 1) == 2