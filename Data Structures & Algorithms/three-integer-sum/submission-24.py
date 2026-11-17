class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # [-4, -1, -1, 0, 1, 2]        
        n = len(nums)
        res = []
        for cur in range(n - 2):
            if cur != 0 and nums[cur - 1] == nums[cur]:
                continue
            left = cur + 1
            right = n - 1
            while left < right:
                while cur + 1 < left < right and nums[left - 1] == nums[left]:
                    left += 1
                while left < right < cur - 1 and nums[right + 1] == nums[right]:
                    right -= 1
                if left >= right:
                    break
                summa = nums[left] + nums[right] + nums[cur]
                if summa == 0:
                    res.append([nums[cur], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif summa < 0:
                    left += 1
                else:
                    right -= 1
        return res