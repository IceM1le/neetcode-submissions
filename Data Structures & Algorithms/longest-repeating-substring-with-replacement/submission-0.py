class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s: return 0
        freq_dict = dict()
        result = 0
        left = 0
        max_freq = 1
        for i in range(len(s)):
            freq_dict[s[i]] = freq_dict.get(s[i], 0) + 1
            max_freq = max(max_freq, freq_dict[s[i]])
            
            while i - left + 1 - max_freq > k:
                freq_dict[s[left]] -= 1
                left += 1
        
            result = max(result, i - left + 1)
        return result