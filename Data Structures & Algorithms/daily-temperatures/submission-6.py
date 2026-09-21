class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                j = stack.pop()[0]
                res[j] = i - j
            stack.append((i, t))
        return res