class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_row = set()
        seen_column = set()
        for i in range(9):
            seen_row.clear()
            seen_column.clear()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in seen_row:
                        return False
                    seen_row.add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in seen_column:
                        return False
                    seen_column.add(board[j][i])
        starts = []
        for i in range(3):
            for j in range(3):
                starts.append((3*i, 3*j))
        for start in starts:
            seen_row.clear()
            for i in range(3):
                for j in range(3):
                    if board[start[0] + i][start[1] + j] != '.':
                        if board[start[0] + i][start[1] + j] in seen_row:
                            return False
                        seen_row.add(board[start[0] + i][start[1] + j])
        return True