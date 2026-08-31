class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = dict()
        for i, num in enumerate(nums):
            if num in dict_nums:
                return [dict_nums[num], i]
            dict_nums[target - num] = i