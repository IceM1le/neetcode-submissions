class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)        
        if n <= 2: return max(nums)
        return max(self.lin_rob(nums[1:], n), self.lin_rob(nums[:-1], n))
    
    def lin_rob(self, nums: List[int], n: int) -> int:
        prev2, prev1 = 0, 0
        for i in range(n-1):
            prev2, prev1 = prev1, max(prev1, prev2 + nums[i])
        return prev1