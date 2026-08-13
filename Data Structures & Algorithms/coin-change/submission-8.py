import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-1] * (amount + 1)
        memo[0] = 0
        
        def dfs(amount):
            if memo[amount] != -1:
                return memo[amount]
            
            res = math.inf

            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            
            memo[amount] = res
            return res
        
        res = dfs(amount)
        return res if res != math.inf else -1