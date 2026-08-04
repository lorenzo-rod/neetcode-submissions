import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [math.inf] * (amount + 1)
        memo[0] = 0

        for i in range(amount):
            for j in coins:
                if i + j <= amount:
                    memo[i + j] = min(memo[i+j], memo[i] + 1)
        
        return memo[amount] if memo[amount] != math.inf else -1
        