class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        gl, lc = nums[0], nums[0]
        for i in range(1, len(nums)):
            lc = max(nums[i], lc + nums[i])
            gl = max(lc, gl)
        return gl