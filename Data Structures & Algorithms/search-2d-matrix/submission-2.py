class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x, y = len(matrix[0]), len(matrix)
        left = 0
        right = x * y - 1
        while left <= right:
            mid = (left + right) // 2
            cur_x, cur_y = mid % x, mid // x
            if matrix[cur_y][cur_x] == target:
                return True
            elif matrix[cur_y][cur_x] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False