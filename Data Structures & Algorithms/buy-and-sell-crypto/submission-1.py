class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        profit = 0
        cur = prices[0]
        for i in range(1, len(prices)):
            if cur > prices[i]:
                cur = prices[i]
            else:
                profit = max(profit, prices[i] - cur)
        return profit