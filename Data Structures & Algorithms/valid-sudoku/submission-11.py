from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                digit = board[i][j]

                if digit == '.':
                    continue

                box_key = (i // 3, j // 3)

                if digit in rows[i] or digit in columns[j] or digit in boxes[box_key]:
                    return False

                rows[i].add(digit)
                columns[j].add(digit)
                boxes[box_key].add(digit)

        
        return True
                
