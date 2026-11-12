class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}${s}" # 5$Hello5$World
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            i = 0
            while s[i] != "$":
                i += 1
            size = int(s[:i])
            i += 1            
            word = s[i:size+i]
            res.append(word)
            s = s[size+i:]
        return res