class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memo = [0 for _ in range(n)]
        memo[0] = 1

        for i in range(m):
            for j in range(n):
                if not((i, j) == (0, 0)):
                    n_i, n_j = i - 1, j - 1
                    a = memo[j] if n_i > -1 else 0
                    b = memo[n_j] if n_j > -1 else 0
                    memo[j] = a + b
        
        return memo[n-1]
