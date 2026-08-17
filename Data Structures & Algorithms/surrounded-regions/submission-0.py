class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board: return
        m, n = len(board), len(board[0])
        regions = set()

        def connecting(i, j):
            if board[i][j] == 'O' and (i, j) not in regions:
                regions.add((i, j))
                for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        connecting(ni, nj)

        for i in range(m):
            if board[i][0] == 'O': connecting(i, 0)
            if board[i][n-1] == 'O': connecting(i, n - 1)
        for i in range(n):
            if board[0][i] == 'O': connecting(0, i)
            if board[m-1][i] == 'O': connecting(m - 1, i)
        for i in range(m):
            for j in range(n):
                if (i, j) not in regions:
                    board[i][j] = 'X'