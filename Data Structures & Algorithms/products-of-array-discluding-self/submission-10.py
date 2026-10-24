class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        k = 1
        n = len(nums)
        res = [1] * n
        for i in range(n):
            res[i] *= k
            k *= nums[i]
        k = 1
        for i in range(n)[::-1]:
            res[i] *= k
            k *= nums[i]
        return res