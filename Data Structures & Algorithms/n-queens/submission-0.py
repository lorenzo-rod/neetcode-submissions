class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diag = set()
        neg_diag = set()
        res = []

        board = [0] * n

        def backtrack(idx):
            if idx == n:
                res.append(board.copy())
                return
            for i in range(n):
                if i in cols:
                    continue
                if idx + i in pos_diag:
                    continue
                if idx - i in neg_diag:
                    continue
                board[idx] = i
                cols.add(i)
                pos_diag.add(idx + i)
                neg_diag.add(idx - i)
                backtrack(idx + 1)
                cols.remove(i)
                pos_diag.remove(idx + i)
                neg_diag.remove(idx - i)
                board[idx] = 0

        backtrack(0)
        
        def buildStr(idx):
            string_list = ["."] * n
            string_list[idx] = 'Q'
            return "".join(string_list)
        
        for i in range(len(res)):
            for j in range(n):
                res[i][j] = buildStr(res[i][j])

        return res