class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter_s, counter_t = dict(), dict()
        for i in range(len(t)):
            num_s, num_t = s[i], t[i]
            counter_t[num_t] = counter_t.get(num_t, 0) + 1
            counter_s[num_s] = counter_s.get(num_s, 0) + 1
        
        return counter_s == counter_t