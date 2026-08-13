class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [0] * (len(s) + 1)
        memo[len(s)] = 1
        
        def dfs(i):
            if i > len(s):
                return 0
            if memo[i] != 0:
                return memo[i]
            if s[i] == '0':
                return 0
        
            res = dfs(i+1)

            if s[i] < '3':
                if i < (len(s) - 1):
                    if s[i] == '1' or s[i+1] < '7':
                        res += dfs(i+2)
            
            memo[i] = res
            return res
        
        return dfs(0)