class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        freq = defaultdict(int)
        res = 0
        n = len(s)
        left = 0
        max_freq = 1
        for right, c in enumerate(s):
            freq[c] += 1
            max_freq = max(max_freq, freq[c])
            
            while right - left + 1 - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res