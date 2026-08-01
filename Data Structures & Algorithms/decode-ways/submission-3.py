class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        memo = [0] * (n + 1)
        memo[-1] = 1

        for i in reversed(range(n)):
            if s[i] != '0':
                memo[i] = memo[i+1]
                if ((i < n - 1)
                    and ((s[i] == '1') or (s[i] == '2' and s[i+1] < '7'))):
                    memo[i] += memo[i+2]
        
        return memo[0]
