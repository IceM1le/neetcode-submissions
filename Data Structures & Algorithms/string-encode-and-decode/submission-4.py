class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += f"{str(len(s))}#{s}"
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        while s:
            i = 0
            c = s[0]
            while s[i] != "#":
                i += 1
            size = int(s[:i])
            word = s[i + 1:size + i + 1]
            result.append(word)
            s = s[size + i + 1:]
        return result