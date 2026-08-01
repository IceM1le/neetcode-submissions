class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero = -1
        for i, num in enumerate(nums):
            if num != 0:
                product *= num
            else:
                if zero != -1:
                    return [0] * len(nums)
                zero = i        
        if zero != -1:  
            result = [0] * len(nums)
            result[zero] = product
        else:
            result = []
            for num in nums:
                result.append(product//num)
        return result
