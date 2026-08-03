class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        left, right = 0, 0
        max_seq = 0        
        n = len(s)
        set_chars = set()
        while right < n:
            while s[right] in set_chars:
                set_chars.remove(s[left])
                left += 1
            set_chars.add(s[right])
            max_seq = max(right - left + 1, max_seq)
            right += 1            
        return max_seq