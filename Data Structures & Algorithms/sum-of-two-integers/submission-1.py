class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 2**31
        MASK = 0xFFFFFFFF

        print(bin(a), bin(b))

        while b:
            carry = ((a & b) << 1) & MASK
            a = (a ^ b) & MASK
            b = carry

        return a if a < MAX else ~(a ^ MASK)