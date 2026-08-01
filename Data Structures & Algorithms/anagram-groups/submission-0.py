class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for i in range(len(strs)):
            string = "".join(sorted(strs[i]))
            result[string] = result.get(string, [])
            result[string].append(strs[i])
        return [v for v in result.values()]