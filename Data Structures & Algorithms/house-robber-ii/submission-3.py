class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) <= 2: return max(nums)
        return max(self.lin_rob(nums[1:]), self.lin_rob(nums[:-1]))
    
    def lin_rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0
        for i in range(len(nums)):
            prev2, prev1 = prev1, max(prev1, prev2 + nums[i])
        return prev1