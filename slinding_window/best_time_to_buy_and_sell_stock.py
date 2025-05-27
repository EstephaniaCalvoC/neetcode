from typing import List


def maxProfit(prices: List[int]) -> int:
    l = 0
    r = 1

    max_profit = 0

    while r < len(prices):
        dif = prices[r] - prices[l]

        if dif <= 0 and r - l == 1:
            l += 1
            r += 1
        elif dif <= 0:
            l += 1
        else:
            max_profit = dif if dif > max_profit else max_profit
            r += 1

    return max_profit


if __name__ == "__main__":
    print(maxProfit([10,1,5,6,7,1])) # 6
    print(maxProfit([10,8,7,5,2])) # 0
    print(maxProfit([10,4,5,1,5,6,7,1])) # 6
    print(maxProfit([7,1,5,3,6,4])) # 5