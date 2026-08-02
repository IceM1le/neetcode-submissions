class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        set_nums = set(nums)
        starters = []
        for num in set_nums:
            if num - 1 not in set_nums and num in set_nums:
                starters.append(num)
        max_count = 1
        for st in starters:
            counter = 0
            cur = st
            while cur in set_nums:
                cur += 1
                counter += 1
            max_count = max(max_count, counter)
        return max_count