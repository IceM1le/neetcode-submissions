class Solution:
    def trap(self, height: List[int]) -> int:
        max_h = 0
        prev_h = [0]
        result = 0
        volume = 0
        distance = {0: 0}
        for i in range(len(height)):
            cur = height[i]
            if cur >= max_h:
                max_h = cur
                prev_h = []
                result += volume
                volume = 0
                distance = {}
            else:
                if i != 0 and height[i - 1] < cur:
                    h = prev_h.pop() if len(prev_h) > 0 else max_h
                    volume_res = (min(h, cur) - height[i - 1]) * distance.get(cur - 1, 0)
                    distance[cur - 1] = 0
                    volume -= volume_res
                    result += volume_res
                elif i != 0 and height[i - 1] > cur:
                    prev_h.append(height[i - 1])
                for i in range(cur, max_h + 1):
                    distance[i] = distance.get(i, 0) + 1
                volume += max_h - cur
        return result