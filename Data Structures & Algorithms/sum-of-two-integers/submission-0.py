class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            tmp = (a ^ b) & MASK
            b = ((a & b) << 1) & MASK
            a = tmp

        return a if a < MAX_INT else ~(a ^ MASK)