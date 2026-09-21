class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}${s}"
        return res #"5$Hello5$World"

    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            n = ""
            i = 0
            while s[i] != "$":
                n += s[i]
                i += 1
            i += 1
            n = int(n)
            word = s[i: i + n]
            res.append(word)
            s = s[i + n:]
        return res