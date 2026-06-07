from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_rows = [set() for _ in range(9)]
        seen_columns = [set() for _ in range(9)]
        seen_boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):

                if board[i][j] == '.':
                    continue

                box_key = (i // 3, j // 3)
                
                if board[i][j] in seen_rows[i] or board[i][j] in seen_columns[j] or board[i][j] in seen_boxes[box_key]:
                    return False
                
                seen_rows[i].add(board[i][j])
                seen_columns[j].add(board[i][j])
                seen_boxes[box_key].add(board[i][j])

        return True
                    