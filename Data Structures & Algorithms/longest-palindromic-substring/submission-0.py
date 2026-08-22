class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
        longest = ""
        for i in range(len(s)):
            odd = self.expand(s, i, i)
            if len(odd) > len(longest): longest = odd
            odd = self.expand(s, i, i + 1)
            if len(odd) > len(longest): longest = odd
        return longest
    
    def expand(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            right += 1
            left -= 1
        return s[left + 1: right]