class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights: return 0
        left, right = 0, len(heights) - 1
        max_V = 0
        while left < right:
            h = min(heights[left], heights[right])
            V = h * (right - left)
            max_V = max(max_V, V)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return max_V