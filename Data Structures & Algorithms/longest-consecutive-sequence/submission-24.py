class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        set_nums = set(nums)
        max_seq = 1
        for i, num in enumerate(nums):
            if num - 1 not in set_nums:
                cur = num
                while cur in set_nums:
                    cur += 1
                max_seq = max(max_seq, cur - num)
        return max_seq