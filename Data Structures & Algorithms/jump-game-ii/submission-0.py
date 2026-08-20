class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        current_end = 0      # конец текущего уровня
        farthest = 0          # самая дальняя достижимая позиция
        
        for i in range(n - 1):   # не обрабатываем последний индекс
            farthest = max(farthest, i + nums[i])
            
            if i == current_end:   # дошли до конца текущего уровня
                jumps += 1
                current_end = farthest
                
                if current_end >= n - 1:
                    break
        
        return jumps