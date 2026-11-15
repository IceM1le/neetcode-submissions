class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set()
        set_nums = set(nums)
        res = 0
        for i, num in enumerate(nums):
            if num - 1 not in set_nums:
                cur = num
                while cur in set_nums:
                    visited.add(cur)
                    cur += 1
                res = max(res, cur - num)
        return res