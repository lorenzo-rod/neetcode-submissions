class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = {}
        
        def dfs(i):
            if i == n:
                return True
            if i in memo:
                return memo[i]
            
            for word in wordDict:
                k = len(word)
                if i + k < n + 1 and s[i:i+k] == word:
                    memo[i] = dfs(i+k)
                    if memo[i]:
                        return True
            
            memo[i] = False
            return False
        
        return dfs(0)