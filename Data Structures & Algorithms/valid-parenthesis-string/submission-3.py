class Solution:
    def checkValidString(self, s: str) -> bool:
        
        n = len(s)
        memo = {}

        def dfs(i, opened, closed):
            if closed > opened:
                return False

            if i == n:
                return opened == closed
            
            if (i, opened, closed) in memo:
                return memo[(i, opened, closed)]
            
            if s[i] == "(":
                if dfs(i + 1, opened + 1, closed):
                    memo[(i, opened, closed)] = True
                    return True
            elif s[i] == ")":
                if dfs(i + 1, opened, closed + 1):
                    memo[(i, opened, closed)] = True
                    return True
            else:
                if dfs(i + 1, opened + 1, closed) or dfs(i + 1, opened, closed + 1) or dfs(i + 1, opened, closed):
                    memo[(i, opened, closed)] = True
                    return True
            
            memo[(i, opened, closed)] = False
            return False

        return dfs(0, 0, 0)
