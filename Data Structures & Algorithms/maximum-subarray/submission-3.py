class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        global_max, local_max = nums[0], nums[0]
        for i in range(1, len(nums)):
            local_max = max(nums[i], local_max + nums[i])
            global_max = max(local_max, global_max)
        return global_max
