class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        m = len(matrix)
        n = len(matrix[0])
        visited = set()
        computed = {}
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
                    if (n_i, n_j) not in visited:
                        visited.add((n_i, n_j))
                        if (n_i, n_j) in computed:
                            res = max(res, 1 + computed[(n_i, n_j)])
                        else:
                            computed[(n_i, n_j)] = dfs(n_i, n_j)
                            res = max(res, 1 + computed[(n_i, n_j)])
                        visited.discard((n_i, n_j))
            return res
        
        for i in range(m):
            for j in range(n):
                computed[(i, j)] = dfs(i, j) if (i, j) not in computed else computed[(i, j)]
                res = max(res, computed[(i, j)])
        
        return res + 1

        