class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:        
        for i in range(len(board)):
            duplicates_h, duplicates_v, duplicates_xy = set(), set(), set()
            for j in range(len(board)):
                cur = board[i][j]
                if cur in duplicates_h:
                    return False
                if cur != ".":
                    duplicates_h.add(cur)

                cur = board[j][i]
                if cur in duplicates_v:
                    return False
                if cur != ".":
                    duplicates_v.add(cur)
                

                x = j % 3 + 3 * (i % 3)
                y = j // 3 + 3 * (i // 3)
                cur = board[x][y]                
                if cur in duplicates_xy:
                    return False
                if cur != ".":
                    duplicates_xy.add(cur)
        return True