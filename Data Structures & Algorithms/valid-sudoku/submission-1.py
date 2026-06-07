class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums_set = set()
        for i in range(9):
            nums_set.clear()
            for j in range(9):
                if board[i][j] in nums_set:
                    print(board[i][j])
                    return False
                if board[i][j] != '.':
                    nums_set.add(board[i][j])
        for j in range(9):
            nums_set.clear()
            for i in range(9):
                if board[i][j] in nums_set:
                    print(board[i][j])
                    return False
                if board[i][j] != '.':
                    nums_set.add(board[i][j])
        for offset in [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]:
            nums_set.clear()
            for i in range(3):
                for j in range(3):
                    if board[offset[0] + i][offset[1] + j] in nums_set:
                        print(board[offset[0] + i][offset[1] + j])
                        return False
                    if board[offset[0] + i][offset[1] + j] != '.':
                        nums_set.add(board[offset[0] + i][offset[1] + j])
        return True