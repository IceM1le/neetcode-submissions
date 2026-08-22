class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s: return 0
        count = 0
        for i in range(len(s)):
            count += self.expand(s, i, i)
            count += self.expand(s, i, i + 1)
        return count
    def expand(self, s: str, left: int, right: int) -> int:
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            count += 1
        return count