class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        min_v = prices[0]
        for i in range(1, len(prices)):
            cur = prices[i]
            if cur < min_v:
                min_v = cur
                continue
            max_profit = max(cur - min_v, max_profit)
        return max_profit