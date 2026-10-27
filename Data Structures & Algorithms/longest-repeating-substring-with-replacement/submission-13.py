class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        visited = defaultdict(int)
        left = 0
        max_len = 0
        res = 0
        n = len(s)
        for right in range(n):
            visited[s[right]] += 1
            max_len = max(max_len, visited[s[right]])

            while right - left + 1 - k > max_len:
                visited[s[left]] -= 1                
                left += 1
            
            res = max(res, right - left + 1)
        return res