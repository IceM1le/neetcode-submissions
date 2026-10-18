class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return True
        n = len(nums)
        max_s = 0
        for i in range(n):
            if max_s < i:
                return False
            max_s = max(max_s, nums[i] + i)
            if max_s >= n:
                return True
        return max_s == n - 1