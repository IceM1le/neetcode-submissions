class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        freq = defaultdict(int)
        left = 0
        res = 0
        longest = 0
        for right, val in enumerate(s):
            freq[val] += 1
            longest = max(longest, freq[val])
            while right - left + 1 - longest > k:
                freq[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res