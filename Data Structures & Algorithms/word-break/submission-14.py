class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = {n : True}
        
        def dfs(i):
            if i in memo:
                return memo[i]
            if i > n:
                return False
            
            for word in wordDict:
                if i + len(word) <= n:
                    if s[i:i+len(word)] == word:
                        if dfs(i+len(word)):
                            memo[i+len(word)] = True
                            return True
            
            memo[i+len(word)] = False
            return False
        
        return dfs(0)