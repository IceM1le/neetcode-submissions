class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []
        m, n = len(heights[0]), len(heights)
        def add_to_set(i, j, ocean):
            if (i, j) not in ocean:
                ocean.add((i, j))
                for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < n and 0 <= nj < m and heights[i][j] <= heights[ni][nj]:
                        add_to_set(ni, nj, ocean)
        atlantic, pacific = set(), set()
        for i in range(m):
            add_to_set(0, i, pacific)
            add_to_set(n - 1, i, atlantic)
        for j in range(n):
            add_to_set(j, 0, pacific)
            add_to_set(j, m - 1, atlantic)
        return [list(lst) for lst in atlantic & pacific]