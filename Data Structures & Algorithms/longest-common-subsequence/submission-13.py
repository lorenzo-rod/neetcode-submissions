class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m = len(text1)
        n = len(text2)
        memo = [0 for _ in range(n+1)]

        for i in reversed(range(m)):
            prev_memo = memo.copy()
            for j in reversed(range(n)):

                if text1[i] == text2[j]:
                    memo[j] = 1 + prev_memo[j+1]
                else:
                    memo[j] = max(prev_memo[j], memo[j+1])
        
        return memo[0]
