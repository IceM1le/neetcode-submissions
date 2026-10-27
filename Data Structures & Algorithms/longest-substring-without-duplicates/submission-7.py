class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        n = len(s)
        visited = set()
        longest = 0
        while right < n:
            if s[right] not in visited:
                visited.add(s[right])
                right += 1
            else:
                visited.remove(s[left])
                left += 1
            longest = max(longest, right - left)
        return longest