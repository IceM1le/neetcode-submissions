class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:        
        max_len = 0
        set_nums = set(nums)
        for num in nums:
            if num - 1 not in set_nums:
                count = 0
                cur = num
                while cur in set_nums:
                    cur += 1
                    count += 1
                max_len = max(max_len, count)
        return max_len