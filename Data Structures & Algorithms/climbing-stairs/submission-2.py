class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1: return 1
        prev1, prev2 = 1, 1
        for i in range(2, n):
            prev1, prev2 = prev2, prev1 + prev2            
        return prev1 + prev2