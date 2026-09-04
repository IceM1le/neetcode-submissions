class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        freq = defaultdict(int)
        left = 0
        res = 0
        max_freq = 1
        for right, val in enumerate(s):
            freq[val] += 1
            max_freq = max(max_freq, freq[val])
            while right - left + 1 - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res