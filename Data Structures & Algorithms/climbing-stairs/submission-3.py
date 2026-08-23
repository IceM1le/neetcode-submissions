class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1: return 1
        prev2, prev1 = 1, 1
        for i in range(1, n):
            prev1, prev2 = prev1 + prev2, prev1
        return prev1