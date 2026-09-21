class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        freq = Counter(s)
        for c in t:            
            freq[c] -= 1
            if freq[c] == -1: return False
        return sum(freq.values()) == 0