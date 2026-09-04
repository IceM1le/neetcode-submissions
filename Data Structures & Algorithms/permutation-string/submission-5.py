class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict, Counter
        freq = Counter(s1)
        n = len(s1)
        count = defaultdict(int)
        left = 0
        for right, val in enumerate(s2):
            count[val] += 1
            if right - left + 1 > n:
                count[s2[left]] -= 1
                if count[s2[left]] == 0: del count[s2[left]]
                left += 1
            if freq == count: return True
        return False