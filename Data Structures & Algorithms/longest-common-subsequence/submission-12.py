class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m = len(text1)
        n = len(text2)
        memo = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in reversed(range(m)):
            for j in reversed(range(n)):

                if text1[i] == text2[j]:
                    memo[i][j] = 1 + memo[i+1][j+1]
                else:
                    memo[i][j] = max(memo[i+1][j], memo[i][j+1])
        
        return memo[0][0]
