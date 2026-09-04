class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, 0
        from collections import Counter, defaultdict
        freq = Counter(s1)
        count = defaultdict(int)
        left = 0
        n = len(s1)
        for right, val in enumerate(s2):
            count[val] += 1
            if right - left + 1 > n:
                count[s2[left]] -= 1
                if count[s2[left]] == 0: del count[s2[left]]
                left += 1
            if len(count) == len(freq) and count == freq: return True
        return False