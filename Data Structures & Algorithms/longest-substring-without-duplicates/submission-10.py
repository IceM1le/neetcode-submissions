class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        left = 0
        n = len(s)
        res = 0
        visited = set()
        for right in range(n):
            while s[right] in visited:
                visited.remove(s[left])
                left += 1
            visited.add(s[right])
            res = max(res, len(visited))
        return res