class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums: return []
        n = len(nums)
        res = [1] * n
        cur = 1
        for i, num in enumerate(nums):
            res[i] *= cur
            cur *= num
        cur = 1
        for i in range(n - 1, -1, -1):
            res[i] *= cur
            cur *= nums[i]
        return res