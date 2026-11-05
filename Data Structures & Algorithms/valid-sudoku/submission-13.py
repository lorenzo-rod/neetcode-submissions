from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        rows = [set() for _ in range(n)]
        columns = [set() for _ in range(n)]
        boxes = defaultdict(set)

        for i in range(n):
            for j in range(n):
                digit = board[i][j]

                if digit == ".":
                    continue
                
                if digit in rows[i]:
                    return False
                
                if digit in columns[j]:
                    return False
                
                box_key = (i // 3, j // 3)

                if digit in boxes[box_key]:
                    return False

                rows[i].add(digit)
                columns[j].add(digit)
                boxes[box_key].add(digit)

        return True
