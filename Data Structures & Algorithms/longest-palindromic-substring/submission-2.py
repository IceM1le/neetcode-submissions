class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
        n = len(s)
        longest = ""
        for i in range(n):
            odd = self.expand(s, i, i)
            if len(longest) < len(odd): longest = odd
            odd = self.expand(s, i, i + 1)
            if len(longest) < len(odd): longest = odd
        return longest

    def expand(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            right += 1
            left -= 1
        return s[left + 1: right]