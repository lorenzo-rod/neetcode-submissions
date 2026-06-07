class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            seen.clear()
            for j in range(9):
                if board[i][j] in seen:
                    return False
                if board[i][j] != '.':
                    seen.add(board[i][j])
        for j in range(9):
            seen.clear()
            for i in range(9):
                if board[i][j] in seen:
                    return False
                if board[i][j] != '.':
                    seen.add(board[i][j])
        for offset in [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]:
            seen.clear()
            for i in range(3):
                for j in range(3):
                    if board[offset[0] + i][offset[1] + j] in seen:
                        return False
                    if board[offset[0] + i][offset[1] + j] != '.':
                        seen.add(board[offset[0] + i][offset[1] + j])
        return True