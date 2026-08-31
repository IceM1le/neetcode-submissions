class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        if not nums: return []
        n = len(nums)
        res = [1] * n
        pointer = 1        
        for i, val in enumerate(nums):
            res[i] *= pointer
            pointer *= val
        pointer = 1        
        for i in range(n)[::-1]:
            res[i] *= pointer
            pointer *= nums[i]       
        return res