class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        if not nums: return []
        n = len(nums)
        res = [1] * n
        pointer = 1
        for i in range(n):
            res[i] *= pointer
            pointer *= nums[i]
        pointer = 1
        for i in range(n)[::-1]:
            res[i] *= pointer
            pointer *= nums[i]            
        return res