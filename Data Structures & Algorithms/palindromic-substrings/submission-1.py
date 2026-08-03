class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0
        n = len(s)

        for i in range(n):
            l = r = i

            while ((-1 < l) and (r < n) and (s[l] == s[r])):
                res += 1
                l -= 1
                r += 1
            
        for i in range(n):
            l, r = i, i + 1

            while ((-1 < l) and (r < n) and (s[l] == s[r])):
                res += 1
                l -= 1
                r += 1
        
        return res