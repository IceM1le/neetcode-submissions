class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed))
        stack = []
        for pos, spd in pairs:                     
            steps = (target - pos) / spd
            while stack and stack[-1] <= steps:                
                stack.pop() 
            stack.append(steps)        
        return len(stack)        