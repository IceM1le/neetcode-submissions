class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        set_nums = set(nums)
        max_seq = 1
        for i in range(n):
            cur = nums[i]
            if not cur - 1 in set_nums and cur + 1 in set_nums:
                seq = 0
                while cur in set_nums:
                    cur += 1
                    seq += 1
                max_seq = max(seq, max_seq)
        return max_seq