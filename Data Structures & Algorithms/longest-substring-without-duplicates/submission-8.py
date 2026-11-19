class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        visited = set()
        n = len(s)
        max_substring = 0
        for right in range(n):
            while left <= right and s[right] in visited:
                visited.remove(s[left])
                left += 1
            visited.add(s[right])
            right += 1
            max_substring = max(max_substring, len(visited))
        return max_substring