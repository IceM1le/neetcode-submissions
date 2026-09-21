class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left = 0
        max_len = 0
        for right, c in enumerate(s):
            while c in chars:
                chars.remove(s[left])
                left += 1            
            chars.add(c)
            max_len = max(max_len, right - left + 1)
        return max_len