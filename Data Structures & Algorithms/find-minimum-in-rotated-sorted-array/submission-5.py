class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums: return 0
        left, right = 0, len(nums) - 1
        min_val = nums[0]
        while left < right:
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid
        return nums[left]