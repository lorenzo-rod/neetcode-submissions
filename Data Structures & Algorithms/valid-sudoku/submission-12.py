class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows = [set() for _ in range(n)]
        columns = [set() for _ in range(n)]
        sqr_n = int(n ** 0.5)
        boxes = [[set() for _ in range(sqr_n)] for _ in range(sqr_n)]

        for i in range(n):
            for j in range(n):
                
                digit = board[i][j]

                if digit == ".":
                    continue

                box_key = (i // sqr_n, j // sqr_n)

                if digit in rows[i] or digit in columns[j] or digit in boxes[box_key[0]][box_key[1]]:
                    return False
                
                rows[i].add(digit)
                columns[j].add(digit)
                boxes[box_key[0]][box_key[1]].add(digit)

        return True