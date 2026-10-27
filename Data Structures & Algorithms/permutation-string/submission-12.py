class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter, defaultdict
        n = len(s1)
        freq = Counter(s1)
        cur = defaultdict(int)
        left = 0
        for right, num in enumerate(s2):
            cur[num] += 1
            if right - left + 1 > n:
                cur[s2[left]] -= 1                
                if cur[s2[left]] == 0:
                    del cur[s2[left]]
                left += 1
            if cur == freq:
                return True
        return False