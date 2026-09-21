class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        set_nums = set(nums)
        max_seq = 1
        visited = set()
        for num in nums:
            if not num - 1 in set_nums and num + 1 in set_nums:
                cur = num
                while cur in set_nums: cur += 1           
                max_seq = max(max_seq, cur - num)
        return max_seq