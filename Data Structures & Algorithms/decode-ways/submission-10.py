class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        memo, memo_1 = 0, 1

        for i in reversed(range(n)):
            if s[i] == '0':
                memo = 0
                memo_2, memo_1 = memo_1, memo
                continue

            memo = memo_1

            if i < n - 1:
                if ((s[i] == '1')
                    or (s[i] == '2' and s[i+1] < '7')):
                    memo += memo_2
            memo_2, memo_1 = memo_1, memo
            
        return memo
        