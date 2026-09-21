class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter, defaultdict
        freq = Counter(s1)
        left = 0
        cur_freq = defaultdict(int)
        n = len(s1)
        for right, val in enumerate(s2):
            cur_freq[val] += 1
            if right + 1 > n:
                cur_freq[s2[left]] -= 1
                if cur_freq[s2[left]] == 0: del cur_freq[s2[left]]
                left += 1
            if cur_freq == freq: return True
        return False