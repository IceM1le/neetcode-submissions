class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix[0]) - 1, len(matrix) - 1
        cur = 0
        while 0 <= m and cur <= n:
            val = matrix[cur][m]
            if val == target:
                return True
            elif val < target:
                cur += 1
            else:
                m -= 1
        return False