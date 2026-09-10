import math
class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = - 2**31
        
        res = 0
        negative = x < 0
        x = abs(x)

        while x:
            digit = x % 10
            x = x // 10

            if res > MAX_INT // 10 or (res == MAX_INT and digit > MAX % 10):
                return 0
            
            res = res * 10 + digit
        
        return res if not negative else -res