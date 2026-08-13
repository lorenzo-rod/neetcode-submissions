class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = [0] * (n + 1)
        memo[n] = 1

        for i in reversed(range(n)):
            if s[i] == '0':
                continue
                
            memo[i] = memo[i+1]

            if s[i] < '3':
                if i < (len(s) - 1):
                    if s[i] == '1' or s[i+1] < '7':
                        memo[i] += memo[i+2]
        
        return memo[0]
        