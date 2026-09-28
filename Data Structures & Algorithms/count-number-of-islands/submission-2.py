class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:        
        if not grid: return 0
        m, n = len(grid[0]), len(grid)
        def find_island(i, j):
            if 0 <= i < n and 0 <= j < m and grid[i][j] == '1':
                grid[i][j] = '0'
                for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                    ni = i + di
                    nj = j + dj
                    find_island(ni, nj)
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    find_island(i, j)
                    count += 1
        return count