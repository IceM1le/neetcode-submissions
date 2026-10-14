class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost: return 0
        n = len(cost)
        if n <= 2: return min(cost)
        prev1, prev2 = 0, 0
        for i in range(2, n + 1):
            prev1, prev2 = prev2, min(prev2 + cost[i - 1], prev1 + cost[i - 2])
        return prev2