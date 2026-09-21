class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        max_len = 0
        counter = 0
        left = 0
        for c in s:
            while c in chars: 
                chars.remove(s[left])
                left += 1
                counter -= 1
            chars.add(c)
            counter += 1
            max_len = max(max_len, counter)
        return max_len