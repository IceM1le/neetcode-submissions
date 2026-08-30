class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_sum = {}
        for i, num in enumerate(nums):
            if target - num in dict_sum:
                return [dict_sum[target - num], i]
            dict_sum[num] = i