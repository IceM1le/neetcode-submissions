class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        x, y = m - 1, 0                            
        while x >= 0 and y < n:
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] < target:
                y += 1
            else:
                x -= 1
        return False