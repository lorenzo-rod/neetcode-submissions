class Solution:
    def numDecodings(self, s: str) -> int:

        memo = [-1] * (len(s) + 1)
        memo[len(s)] = 1

        def calcNumDecodings(idx):
            if memo[idx] != -1:
                return memo[idx]
            if int(s[idx]) == 0:
                memo[idx] = 0
                return memo[idx]
            if idx < len(s) - 1 and (
                int(s[idx]) == 1 or (int(s[idx]) == 2 and -1 < int(s[idx + 1]) < 7)
            ):
                memo[idx] = calcNumDecodings(idx + 1) + calcNumDecodings(idx + 2)
                return memo[idx]
            memo[idx] = calcNumDecodings(idx + 1)
            return memo[idx]

        return calcNumDecodings(0)
