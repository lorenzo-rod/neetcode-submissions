class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        visited = set()
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def dfs(i, j):
            if not (-1 < i < len(board)):
                return
            if not (-1 < j < len(board[0])):
                return
            if (i, j) in visited:
                return
            if board[i][j] != 'O':
                return

            visited.add((i, j))

            for dx, dy in directions:
                dfs(i + dx, j + dy)

        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[0]) - 1)

        for j in range(len(board[0])):
            dfs(0, j)
            dfs(len(board) - 1, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in visited:
                    board[i][j] = 'X'
        
