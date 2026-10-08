class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])
        visited = set()
        def connecting(i, j):
            if (i, j) not in visited:
                visited.add((i, j))
                for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == "O":
                        connecting(ni, nj)

        for i in range(n):
            if board[i][0] == "O":
                connecting(i, 0)
            if board[i][m - 1] == "O":
                connecting(i, m - 1)
        for j in range(m):
            if board[0][j] == "O":
                connecting(0, j)
            if board[n - 1][j] == "O":
                connecting(n - 1, j)
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and board[i][j] == "O":
                    board[i][j] = "X"