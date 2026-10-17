class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        pos = 0
        for i in range(n):
            if pos < i: return False
            pos = max(pos, nums[i] + i)
            if pos >= n - 1:
                return True
        return pos == n - 1