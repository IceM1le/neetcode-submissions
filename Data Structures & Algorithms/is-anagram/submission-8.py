class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = Counter(t)
        for c in s:            
            freq[c] -= 1
            if freq[c] == 0:
                del freq[c]
        return len(freq) == 0