class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = ((1, 0), (0, -1), (0, 1), (-1, 0))
        n = len(word)
        visited = set()

        def dfs(i, j, k):
            if k == n:
                return True
            if not(-1 < i < len(board)):
                return False
            if not(-1 < j < len(board[0])):
                return False
            if board[i][j] != word[k]:
                return False
            
            visited.add((i, j))

            for dx, dy in directions:
                n_i, n_j = i + dx, j + dy
                if (n_i, n_j) not in visited:
                    if dfs(n_i, n_j, k + 1):
                        return True
            
            visited.discard((i, j))

            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        
        return False

