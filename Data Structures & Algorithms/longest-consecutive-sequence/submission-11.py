class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        set_nums = set(nums)
        max_count = 1    
        for num in nums:
            if not num - 1 in set_nums and num + 1 in set_nums:
                cur = num
                while cur in set_nums:
                    cur += 1
                max_count = max(max_count, cur - num)
        return max_count