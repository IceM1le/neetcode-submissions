class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        dict_anagrams = defaultdict(list)
        for s in strs:
            dict_anagrams["".join(sorted(s))].append(s)
        return [v for v in dict_anagrams.values()]