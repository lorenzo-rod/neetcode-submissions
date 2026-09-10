class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = - MAX_INT - 1

        if x == MIN_INT:
            return 0

        res = 0
        negative = x < 0
        x = abs(x)
        LIMIT = MAX_INT // 10
        MAX_DIGIT = MAX_INT % 10

        while x:
            digit = x % 10
            x = x // 10

            if res > LIMIT or (res == LIMIT and digit > MAX_DIGIT):
                return 0
            
            res = res * 10 + digit
        
        return res if not negative else -res