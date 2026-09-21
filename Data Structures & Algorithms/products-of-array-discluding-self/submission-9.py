class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums: return []
        n = len(nums)
        div = 1
        res = [1] * n
        for i in range(n):
            res[i] *= div
            div *= nums[i]
        div = 1
        for i in range(n)[::-1]:
            res[i] *= div
            div *= nums[i]
        return res