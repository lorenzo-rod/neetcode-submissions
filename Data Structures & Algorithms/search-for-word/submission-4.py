class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(i, j, index):
            if i < 0 or i >= len(board):
                return
            if j < 0 or j >= len(board[0]):
                return
            if board[i][j] != word[index]:
                return
            elif index == len(word) - 1:
                return True
            
            for dx, dy in directions:
                tmp, board[i][j] = board[i][j], "#"
                if dfs(i + dx, j + dy, index + 1):
                    return True
                board[i][j] = tmp
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        
        return False