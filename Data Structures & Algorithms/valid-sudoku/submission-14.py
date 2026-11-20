from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):

                digit = board[i][j]

                if digit == ".":
                    continue
                
                if digit in rows[i]:
                    return False
                
                if digit in columns[j]:
                    return False

                box_id = (i // 3, j // 3)

                if digit in boxes[box_id]:
                    return False

                rows[i].add(digit)
                columns[j].add(digit)
                boxes[box_id].add(digit)

        return True
