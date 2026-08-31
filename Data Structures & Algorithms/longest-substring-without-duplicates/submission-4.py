class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        left, right = 0, 0
        visited = set()
        max_substring = 1
        while right < len(s):
            while s[right] in visited:
                visited.remove(s[left])
                left += 1
            visited.add(s[right])
            max_substring = max(max_substring, right - left + 1)
            right += 1
        return max_substring