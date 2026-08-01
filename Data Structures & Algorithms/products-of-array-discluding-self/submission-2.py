class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        pointer = 1
        for i in range(n):
            result[i] *= pointer
            pointer *= nums[i] 
        
        pointer = 1
        for i in range(n)[::-1]:
            result[i] *= pointer
            pointer *= nums[i] 
        return result