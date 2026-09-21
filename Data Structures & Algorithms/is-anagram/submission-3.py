class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        freq1 = Counter(s)
        freq2 = Counter(t)
        return freq1 == freq2