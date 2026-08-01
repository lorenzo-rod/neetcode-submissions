class Solution:
    def numDecodings(self, s: str) -> int:

        memo = {len(s) : 1}
        
        def add(i):
            if i in memo:
                return memo[i]
            if s[i] == '0':
                return 0

            res = add(i+1)
            if ((i < len(s) - 1)
                and ((s[i] == '1') or (s[i] == '2' and s[i+1] < '7'))):
                res += add(i+2)
            
            memo[i] = res
            return res
        
        return add(0)