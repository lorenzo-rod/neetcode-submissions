class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        if n < m:
            return 0

        memo = [0 for _ in range(m+1)]
        memo[m] = 1

        for i in reversed(range(n)):
            prev = memo.copy()
            for j in reversed(range(m)):

                if s[i] == t[j]:
                    memo[j] += prev[j+1]
            
        return memo[0]
        
        