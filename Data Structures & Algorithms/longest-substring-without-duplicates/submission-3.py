class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        left = 0
        max_seq = 0        
        n = len(s)
        set_chars = set()
        for i in range(n):
            while s[i] in set_chars:
                set_chars.remove(s[left])
                left += 1
            set_chars.add(s[i])
            max_seq = max(i - left + 1, max_seq)                    
        return max_seq