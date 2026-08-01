class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = dict()
        for i in range(len(nums)):
            if target - nums[i] in counter:
                return [counter[target - nums[i]], i]
            counter[nums[i]] = i
