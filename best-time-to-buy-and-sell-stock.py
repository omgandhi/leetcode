# 121
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    if n < 2:
        return 0
    currMaxProfit, minStock = float('-inf'), prices[0]
    for p in prices:
        currMaxProfit = max(currMaxProfit, p - minStock)
        minStock = min(minStock, p)
    return currMaxProfit
