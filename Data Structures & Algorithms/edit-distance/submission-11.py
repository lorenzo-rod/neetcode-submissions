class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n1 = len(word1)
        n2 = len(word2)

        memo = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        for i in range(n1 + 1):
            memo[i][n2] = n1 - i
        for j in range(n2 + 1):
            memo[n1][j] = n2 - j
        
        for i in reversed(range(n1)):
            for j in reversed(range(n2)):

                if word1[i] == word2[j]:
                    memo[i][j] = memo[i+1][j+1]
                else:
                    memo[i][j] = 1 + min(memo[i][j+1], memo[i+1][j], memo[i+1][j+1])
        
        return memo[0][0]
