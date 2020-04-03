"""
Given a array of numbers representing the stock prices of a company in
 chronological order, write a function that calculates the maximum profit
 you could have made from buying and selling that stock once.
 You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, 
since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""

def calculateMaxProfit(s: list) -> int:
    assert len(s) >= 2
    max_profit = 0
    for i in range(1, len(s)):
        point_profit = max(s[i:])-min(s[:i])
        if point_profit > max_profit:
            max_profit = point_profit
    return max_profit

if __name__ == "__main__":
    assert calculateMaxProfit([9, 11, 8, 5, 7, 10]) == 5
    assert calculateMaxProfit([9, 10, 4, 5]) == 1
    assert calculateMaxProfit([12, 4, 3]) == 0
    assert calculateMaxProfit([2, 11, 12, 14, 16, 56]) == 54