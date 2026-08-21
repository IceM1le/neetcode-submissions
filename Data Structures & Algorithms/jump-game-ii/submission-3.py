class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        max_reached = nums[0]
        count = 0
        cur_end = 0
        for i in range(n - 1):
            max_reached = max(max_reached, i + nums[i])
            if cur_end == i:
                cur_end = max_reached
                count += 1
        return count