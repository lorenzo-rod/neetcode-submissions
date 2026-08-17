class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memo = {(0, 0) : 1}
        
        def dfs(i, j):
            if not(-1 < i):
                return 0
            if not(-1 < j):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            memo[(i, j)] = dfs(i-1, j) + dfs(i, j-1)
            return memo[(i, j)]
        
        return dfs(m-1, n-1)