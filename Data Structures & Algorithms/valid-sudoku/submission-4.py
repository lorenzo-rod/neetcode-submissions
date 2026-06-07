class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            seen.clear()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        for i in range(9):
            seen.clear()
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in seen:
                        return False
                    seen.add(board[j][i])
        starts = []
        for i in range(3):
            for j in range(3):
                starts.append((3*i, 3*j))
        for start in starts:
            seen.clear()
            for i in range(3):
                for j in range(3):
                    if board[start[0] + i][start[1] + j] != '.':
                        if board[start[0] + i][start[1] + j] in seen:
                            return False
                        seen.add(board[start[0] + i][start[1] + j])
        return True