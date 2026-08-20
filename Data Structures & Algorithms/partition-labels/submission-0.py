class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i
        start, end = 0, 0
        res = []
        for i in range(len(s)):
            end = max(end, last[s[i]])
            if end == i:
                res.append(end - start + 1)
                start = i + 1
        return res
                