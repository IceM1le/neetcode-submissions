class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_char = dict()
        n = len(s1)
        for i in range(n):
            count_char[s1[i]] = count_char.get(s1[i], 0) + 1
        left, right = 0, 0
        counts = dict()
        for right in range(len(s2)):
            if s2[right] in count_char:
                if not counts: left = right
                counts[s2[right]] = counts.get(s2[right], 0) + 1
                if right - left + 1 == n:
                    if counts == count_char:
                        return True
                    else:
                        counts[s2[left]] -= 1
                        left += 1
            else:
                counts = dict()                
        return False