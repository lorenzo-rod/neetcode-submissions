class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_map = set()
            for j in range(9):
                if board[i][j] in row_map:
                    print(1)
                    return False
                if board[i][j] != '.':
                    row_map.add(board[i][j])
        for j in range(9):
            col_map = set()
            for i in range(9):
                if board[i][j] in col_map:
                    print(2)
                    return False
                if board[i][j] != '.':
                    col_map.add(board[i][j])
        for offset in [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]:
            box_map = set()
            for i in range(3):
                for j in range(3):
                    if board[offset[0] + i][offset[1] + j] in box_map:
                        print(3, offset, board[offset[0] + i][offset[1] + j])
                        return False
                    if board[offset[0] + i][offset[1] + j] != '.':
                        box_map.add(board[offset[0] + i][offset[1] + j])
        return True