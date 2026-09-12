class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31 - 1

        if x == - 2**31:
            return 0
        
        negative = x < 0
        x = abs(x)
        res = 0

        while x:
            digit = x % 10
            x = x // 10

            if (res > MAX // 10) or (res == MAX // 10 and digit > MAX % 10):
                return 0
            
            res = res * 10 + digit
        
        return - res if negative else res
