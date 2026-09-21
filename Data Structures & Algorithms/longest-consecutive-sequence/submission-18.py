class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:        
        if not nums: return 0
        set_nums = set(nums)
        max_len = 1
        for num in nums:            
            if not num - 1 in set_nums and num + 1 in set_nums:
                count = 1
                cur = num
                while cur + 1 in set_nums:
                    cur += 1
                    count += 1
                max_len = max(max_len, count)
        return max_len