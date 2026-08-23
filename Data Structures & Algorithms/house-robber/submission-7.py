class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        if n <= 2: return max(nums)
        prev2, prev1 = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            prev2, prev1 = prev1, max(prev1, prev2 + nums[i])
        return prev1