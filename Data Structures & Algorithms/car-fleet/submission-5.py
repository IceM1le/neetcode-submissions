class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dict_speed = {}
        for i, pos in enumerate(position):
            dict_speed[pos] = speed[i]
        position = sorted(position)
        stack = []
        for i, pos in enumerate(position):
            speed[i] = dict_speed[pos]
        dict_speed.clear()
        for i in range(len(position)):            
            steps = (target - position[i]) / speed[i]
            while stack and stack[-1] <= steps:                
                stack.pop() 
            stack.append(steps)        
        return len(stack)