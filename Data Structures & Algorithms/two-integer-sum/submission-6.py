class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_sum = dict()
        for i in range(len(nums)):
            if target - nums[i] in dict_sum:
                return [dict_sum[target - nums[i]], i]
            dict_sum[nums[i]] = i
            