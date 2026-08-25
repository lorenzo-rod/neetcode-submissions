class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def dfs(i, j):
            if not(-1 < i < m):
                return
            if not(-1 < j < n):
                return
            if board[i][j] != 'O':
                return
            
            board[i][j] = '#'
            
            for dx, dy in directions:
                n_i, n_j = i + dx, j + dy
                dfs(n_i, n_j)
        
        for i in range(m):
            dfs(i, n-1)
            dfs(i, 0)
        
        for j in range(n):
            dfs(m-1, j)
            dfs(0, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
