class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed))[::-1]
        res = 0
        stack = []
        for pos, spd in pairs:
            cur = (target - pos) / spd
            if stack and stack[-1] >= cur:
                continue
            stack.append(cur)
        return len(stack)