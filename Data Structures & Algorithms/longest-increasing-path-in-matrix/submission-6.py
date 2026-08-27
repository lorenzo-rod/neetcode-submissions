class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        m = len(matrix)
        n = len(matrix[0])
        computed = [[-1 for _ in range(n)] for _ in range(m)]
        res = 0

        def dfs(i, j):
            res = 0
            for dx, dy in directions:
                n_i, n_j = i + dx, j + dy

                if not(-1 < n_i < m):
                    continue
                
                if not(-1 < n_j < n):
                    continue
                
                if matrix[i][j] < matrix[n_i][n_j]:
                    if computed[n_i][n_j] == -1:
                        computed[n_i][n_j] = dfs(n_i, n_j)
                    res = max(res, 1 + computed[n_i][n_j])
            return res
        
        for i in range(m):
            for j in range(n):
                if computed[i][j] == -1:
                    computed[i][j] = dfs(i, j)
                res = max(res, computed[i][j])
        
        return res + 1

        