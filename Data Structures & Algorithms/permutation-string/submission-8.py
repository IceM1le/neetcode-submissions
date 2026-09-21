class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter, defaultdict
        freq = Counter(s1)
        n = len(s1)
        cur_freq = defaultdict(int)
        left = 0
        for right, c in enumerate(s2):
            cur_freq[c] += 1
            if right - left + 1 > n:
                cur_freq[s2[left]] -= 1
                if cur_freq[s2[left]] == 0:
                    del cur_freq[s2[left]]
                left += 1
            if cur_freq == freq:
                return True
        return False