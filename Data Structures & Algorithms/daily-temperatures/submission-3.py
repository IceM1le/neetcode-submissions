class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures: return []
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and stack[-1][1] <= temperatures[i]:
                stack.pop()
            if stack and stack[-1][1] > temperatures[i]:
                res[i] = stack[-1][0] - i
            stack.append((i, temperatures[i]))
        return res