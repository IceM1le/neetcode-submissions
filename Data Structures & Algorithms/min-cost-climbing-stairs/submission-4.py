class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost: return 0
        n = len(cost)
        if n <= 2: return min(cost)
        prev2, prev1 = 0, 0
        for i in range(2, n + 1):
            prev2, prev1 = prev1, min(prev1 + cost[i - 1], cost[i - 2] + prev2)
        return prev1