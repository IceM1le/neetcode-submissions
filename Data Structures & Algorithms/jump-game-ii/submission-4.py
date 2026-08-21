class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums: return 0
        count = 0
        max_reached = nums[0]
        end = 0
        for i in range(len(nums) - 1):
            max_reached = max(max_reached, nums[i] + i)
            if end == i:
                end = max_reached
                count += 1
        return count