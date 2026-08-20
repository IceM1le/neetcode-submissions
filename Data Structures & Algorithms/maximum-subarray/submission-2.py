class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        max_global = max_local = nums[0]
        for i in range(1, len(nums)):
            max_local = max(max_local + nums[i], nums[i])
            max_global = max(max_global, max_local)
        return max_global