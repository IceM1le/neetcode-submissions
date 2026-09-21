class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        dict_chars = defaultdict(int)
        max_len = 0
        res = 0
        left = 0
        for right in range(len(s)):
            dict_chars[s[right]] += 1
            max_len = max(max_len, dict_chars[s[right]])

            while right - left + 1 - k > max_len:
                dict_chars[s[left]] -= 1
                if dict_chars[s[left]] == 0:
                    del dict_chars[s[left]]
                left += 1
            
            res = max(res, right - left + 1)
        return res