class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(i, j, index, word):
            if i < 0 or i >= len(board):
                return
            if j < 0 or j >= len(board[0]):
                return
            
            if board[i][j] == word[index]:
                if index == len(word) - 1:
                    return True
                tmp = board[i][j]
                board[i][j] = "#"
                for direction in directions:
                    if dfs(i + direction[0], j + direction[1], index + 1, word):
                        return True
                board[i][j] = tmp
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0, word):
                    return True
        
        return False

            
