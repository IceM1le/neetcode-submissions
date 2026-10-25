class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                while right > left > i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                while left < right < n - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                if left >= right:
                    break
                summa = nums[left] + nums[right] + nums[i]
                if summa == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1                    
                    right -= 1
                elif summa < 0:
                    left += 1
                else:
                    right -= 1
        return res