class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = defaultdict(int)
        n = len(s1)
        res = Counter(s1)
        left = 0
        for right, val in enumerate(s2):
            if val not in res:
                left = right + 1
                del freq
                freq = defaultdict(int)
                continue
            freq[val] += 1
            while right - left + 1 > n:
                freq[s2[left]] -= 1
                if freq[s2[left]] == 0:
                    del freq[s2[left]]
                left += 1
            if freq == res:
                return True
        return False