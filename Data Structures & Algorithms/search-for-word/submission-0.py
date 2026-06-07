class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(i, j, idx):
            if idx == len(word):
                return True
            if not(-1 < i < len(board) and -1 < j < len(board[0])):
                return False
            if word[idx] != board[i][j]:
                return False
            
            tmp = board[i][j]
            board[i][j] = "#"

            for dx, dy in directions:
                if dfs(i + dx, j + dy, idx + 1):
                    return True
            
            board[i][j] = tmp

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    res = dfs(i, j, 0)
                    if res:
                        return res

        return False