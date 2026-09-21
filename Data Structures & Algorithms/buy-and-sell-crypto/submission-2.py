class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        profit = 0
        cur = prices[0]
        for price in prices:
            if cur > price:
                cur = price
            else:
                profit = max(profit, price - cur)
        return profit