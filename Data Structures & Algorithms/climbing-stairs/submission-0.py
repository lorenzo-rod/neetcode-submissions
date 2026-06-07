class Solution:
    def climbStairs(self, n: int) -> int:
        c0, c1, c2 = 1, 1, 1
        for i in range(2, n+1):
            c0 = c1 + c2
            c2, c1 = c1, c0
        return c0