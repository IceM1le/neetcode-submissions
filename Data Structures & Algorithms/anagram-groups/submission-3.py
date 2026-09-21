class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        dict_strs = defaultdict(list)
        for s in strs:            
            dict_strs["".join(sorted(s))].append(s)
        return [anagram for anagram in dict_strs.values()]
            