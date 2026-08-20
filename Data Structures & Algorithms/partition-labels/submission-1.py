class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        n = len(s)
        for i in range(n): last[s[i]] = i
        start, end, res = 0, 0, []
        for i in range(n):
            end = max(end, last[s[i]])
            if end == i:
                res.append(end - start + 1)
                start = i + 1
        return res