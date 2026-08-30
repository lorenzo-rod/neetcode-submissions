class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        if n < m:
            return 0

        memo = [0 for _ in range(m+1)]

        for i in reversed(range(n)):
            prev = 1
            for j in reversed(range(m)):

                tmp = memo[j]

                if s[i] == t[j]:
                    memo[j] += prev
                
                prev = tmp
            
        return memo[0]
        
        