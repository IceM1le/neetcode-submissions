class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n - 2):
            cur = nums[i]
            if i != 0 and nums[i - 1] == nums[i]: continue
            left, right = i + 1, n - 1
            while left < right:
                if left != i + 1 and nums[left] == nums[left - 1]: 
                    left += 1
                    continue
                if right != n - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                    continue
                if nums[left] + nums[right] == -cur:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > -cur:
                    right -= 1
                else:
                    left += 1
        return result