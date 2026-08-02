class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        while left < right:            
            if height[left] < height[right]:
                cur = height[left]
                if cur >= max_left:
                    max_left = cur
                else:
                    water += max_left - cur
                left += 1
            else:
                cur = height[right]
                if cur >= max_right:
                    max_right = cur
                else:
                    water += max_right - cur
                right -= 1
        return water