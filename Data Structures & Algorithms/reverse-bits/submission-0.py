class Solution:
    def reverseBits(self, n: int) -> int:
        a = 0
        for i in range(32):
            a = a << 1
            if n & 1:
                a += 1
            n = n >> 1
        return a