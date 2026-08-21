class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        position = 0
        for i in range(n):
            if position < i: return False
            position = max(position, nums[i] + i)
            if position >= n - 1: return True
        return position == n - 1