class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        memo_1, memo_2 = 1, 0

        for i in reversed(range(n)):
            memo = 0
            if s[i] != '0':
                memo = memo_1
                if ((i < n - 1)
                    and ((s[i] == '1') or (s[i] == '2' and s[i+1] < '7'))):
                    memo += memo_2
            memo_2, memo_1 = memo_1, memo
        
        return memo
