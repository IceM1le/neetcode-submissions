class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        idx = 1
        res = [1] * n
        for i, num in enumerate(nums):
            res[i] *= idx
            idx *= num
        idx = 1
        for i in range(n)[::-1]:
            res[i] *= idx
            idx *= nums[i]
        return res