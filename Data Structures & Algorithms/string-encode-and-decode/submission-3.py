class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += f"{chr(len(s))}{s}"
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        while s:
            size = ord(s[0])
            word = s[1:size + 1]
            result.append(word)
            s = s[size + 1:]
        return result