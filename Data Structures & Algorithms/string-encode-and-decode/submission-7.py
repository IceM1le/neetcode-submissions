class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}%{s}" # "5%Hello|5%World"
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            n = ""
            i = 0
            while s[i] != "%":
                n += s[i]
                i += 1
            n = int(n)
            i += 1
            res.append(s[i:i+n])
            s = s[i+n:]
        return res