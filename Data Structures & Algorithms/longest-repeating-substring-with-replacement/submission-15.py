class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        left = res = max_len = 0
        for right, val in enumerate(s):
            freq[val] += 1
            max_len = max(max_len, freq[val])
            while right - left + 1 - k > max_len:
                freq[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res