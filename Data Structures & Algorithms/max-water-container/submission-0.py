class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_volume = 0
        while left < right:
            distance = right - left
            volume = distance * min(heights[left], heights[right])
            if volume > max_volume: max_volume = volume
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return max_volume
            