class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return False
        max_reached = 0
        n = len(nums)
        for i in range(n):
            if i > max_reached: return False
            max_reached = max(i + nums[i], max_reached)            
            if max_reached > n - 1: return True
        return True