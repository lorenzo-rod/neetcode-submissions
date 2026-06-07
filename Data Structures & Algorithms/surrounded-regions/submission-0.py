class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def dfs(i, j):
            board[i][j] = "S"
            stack = [(i, j)]
            while stack:
                i, j = stack.pop()
                for dx, dy in directions:
                    n_i, n_j = i + dx, j + dy
                    if (
                        -1 < n_i < m
                        and -1 < n_j < n
                        and board[n_i][n_j] == "O"
                    ):
                        board[n_i][n_j] = "S"
                        stack.append((n_i, n_j))
        
        for i in range(m):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][n-1] == "O":
                dfs(i, n-1)
        
        for j in range(n):
            if board[0][j] == "O":
                dfs(0, j)
            if board[m-1][j] == "O":
                dfs(m-1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"
