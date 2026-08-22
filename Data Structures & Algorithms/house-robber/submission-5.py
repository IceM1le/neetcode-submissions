class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        if n == 1: return nums[0]

        prev1, prev2 = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            prev2, prev1 = max(prev2, prev1 + nums[i]), prev2
        return prev2