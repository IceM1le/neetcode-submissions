class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        t_counter = Counter(t)
        missing = len(t)
        left = 0
        start, end = 0, len(s) + 1
        for right, char in enumerate(s):
            if t_counter[char] > 0: missing -= 1                
            t_counter[char] -= 1
            while missing == 0:
                if right - left < end - start:
                    start, end = left, right
                t_counter[s[left]] += 1
                if t_counter[s[left]] > 0:
                    missing += 1
                left += 1
        return "" if end == len(s) + 1 else s[start: end + 1]