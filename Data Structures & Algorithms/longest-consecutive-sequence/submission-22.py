class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        set_nums = set(nums)
        visited = set()
        max_seq = 1
        for i, num in enumerate(nums):
            if num not in visited and num + 1 in set_nums:
                visited.add(num)
                cur = num
                while cur in set_nums:
                    cur += 1
                    visited.add(cur)
                max_seq = max(max_seq, cur - num)
        return max_seq