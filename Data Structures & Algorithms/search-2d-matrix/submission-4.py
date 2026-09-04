class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        n = len(matrix[0])
        m = len(matrix)
        x, y = n - 1, 0
        while x >= 0 and y < m:
            if matrix[y][x] == target: return True
            elif matrix[y][x] < target: y += 1
            else: x -= 1
        return False