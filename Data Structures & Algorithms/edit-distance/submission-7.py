class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n1 = len(word1)
        n2 = len(word2)

        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == n1:
                return n2 - j
            if j == n2:
                return n1 - i
            
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i+1, j+1)
                return memo[(i, j)]
            
            memo[(i, j)] = 1 + min(dfs(i, j+1), dfs(i+1, j), dfs(i+1, j+1))
            return memo[(i, j)]
        
        return dfs(0, 0)
