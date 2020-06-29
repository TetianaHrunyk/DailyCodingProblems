"""Find the minimum number of coins required to make n cents.
You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.
For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢."""


def get_coins_required(n):
    coins = [25, 10, 5, 1]
    coins_req = 0
    while n != 0:
        if n - max(coins) >= 0:
            n -= max(coins)
            coins_req += 1
        else:
            coins.remove(max(coins))
    return coins_req

if __name__ == "__main__":
    assert get_coins_required(16) == 3
    assert get_coins_required(22) == 4
    assert get_coins_required(25) == 1
    assert get_coins_required(101) == 5