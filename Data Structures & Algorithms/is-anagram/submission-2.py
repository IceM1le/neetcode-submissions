class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        dict_freq = defaultdict(int)
        for c in s: dict_freq[c] += 1
        for c in t: dict_freq[c] -= 1
        return all(v == 0 for v in dict_freq.values())