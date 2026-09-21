class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 2):
            cur = nums[i]
            left, right = i + 1, n - 1
            if i == 0 or nums[i - 1] != cur:
                while left < right:
                    if left != i + 1 and nums[left] == nums[left - 1]: 
                        left += 1
                        continue
                    if right != n - 1 and nums[right] == nums[right + 1]:
                        right -= 1
                        continue
                    mid = nums[left] + nums[right] + cur                
                    if mid == 0: 
                        res.append([cur, nums[left], nums[right]])
                        left += 1
                        right -= 1
                    elif mid < 0: 
                        left += 1
                    else: 
                        right -= 1
        return res