class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n < 3:
            return n

        dp = 0
        dp_1, dp_2 = 2, 1

        for i in range(2, n):
            dp = dp_1 + dp_2
            dp_2, dp_1 = dp_1, dp
        
        return dp