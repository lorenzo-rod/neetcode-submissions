class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        res = 0
        negative = x < 0
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            if res > (MAX_INT - digit) // 10:
                return 0

            res = res * 10 + digit

        return -res if negative else res
