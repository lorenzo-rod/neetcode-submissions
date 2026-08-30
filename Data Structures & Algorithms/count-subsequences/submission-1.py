class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        if n < m:
            return 0

        memo = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for j in range(m+1):
            memo[n][j] = 0
        for i in range(n+1):
            memo[i][m] = 1

        for i in reversed(range(n)):
            for j in reversed(range(m)):

                memo[i][j] = memo[i+1][j]

                if s[i] == t[j]:
                    memo[i][j] += memo[i+1][j+1]
            
        return memo[0][0]
        
        