class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memo = [[0 for _ in range(n)] for _ in range(m)]
        memo[0][0] = 1

        for i in range(m):
            for j in range(n):
                if not((i, j) == (0, 0)):
                    n_i, n_j = i - 1, j - 1
                    a = memo[n_i][j] if n_i > -1 else 0
                    b = memo[i][n_j] if n_j > -1 else 0
                    memo[i][j] = a + b
        
        return memo[m-1][n-1]

        
        def dfs(i, j):
            if not(-1 < i < m):
                return 0
            if not(-1 < j < n):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            memo[(i, j)] = dfs(i-1, j) + dfs(i, j-1)
            return memo[(i, j)]
        
        return dfs(m-1, n-1)