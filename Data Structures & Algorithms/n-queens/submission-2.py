class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, pos_diag, neg_diag = set(), set(), set()
        board = [0] * n
        res = []

        def backtrack(row):
            if row == n:
                res.append(board[:])
                return
            for col in range(n):
                if col in cols:
                    continue
                if col + row in pos_diag:
                    continue
                if col - row in neg_diag:
                    continue
                cols.add(col)
                pos_diag.add(col + row)
                neg_diag.add(col - row)
                board[row] = col
                backtrack(row + 1)
                board[row] = 0
                neg_diag.remove(col - row)
                pos_diag.remove(col + row)
                cols.remove(col)
        
        backtrack(0)
        
        for i in range(len(res)):
            for j in range(n):
                row = ["."] * n
                row[res[i][j]] = "Q"
                res[i][j] = "".join(row)


        return res