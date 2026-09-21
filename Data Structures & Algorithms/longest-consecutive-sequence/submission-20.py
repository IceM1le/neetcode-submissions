class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        set_nums = set(nums)
        max_len = 1
        for num in nums:
            if num - 1 not in set_nums:
                count = 0
                cur = num
                while cur in set_nums:
                    count += 1
                    cur += 1
                max_len = max(max_len, count)
        return max_len