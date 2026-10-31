class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:    
        n, x, y = len(matrix), len(matrix[0]) - 1, 0
        while x >= 0 and y < n:
            cur = matrix[y][x]
            if cur == target:
                return True
            elif cur > target:
                x -= 1
            else:
                y += 1
        return False