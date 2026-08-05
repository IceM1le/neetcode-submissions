class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_rectangle = 0
        stack = []
        right = [n] * n
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                right[stack.pop()] = i
            stack.append(i)
        stack.clear()
        left = [-1] * n
        for i in range(-1, -n - 1, -1):
            while stack and heights[stack[-1]] > heights[i]:
                left[stack.pop()] = i + n
            stack.append(i + n)
        for i in range(n):
            max_rectangle = max(heights[i] * (right[i] - left[i] - 1), max_rectangle)
        return max_rectangle