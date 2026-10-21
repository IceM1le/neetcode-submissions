class Solution:
    def rob(self, nums: List[int]) -> int:
        def lin_rob(nums: List[int]) -> int:
            prev2, prev1 = 0, 0
            for i in range(n-1):
                prev2, prev1 = prev1, max(prev1, prev2 + nums[i])
            return prev1
        n = len(nums)
        if n <= 2: return max(nums)
        return max(lin_rob(nums[1:]), lin_rob(nums[:-1]))

