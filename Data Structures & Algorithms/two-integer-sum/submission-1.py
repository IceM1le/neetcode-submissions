class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = set(nums)
        counter = dict()
        res = []
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        for i in range(len(nums)):
            num = target - nums[i]
            if (num == nums[i] and counter[num] > 1) or (num in num_set and num != nums[i]):
                res.append(i)
        return res