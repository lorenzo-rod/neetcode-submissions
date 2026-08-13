import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [math.inf] * (amount + 1)
        memo[0] = 0

        for total in range(amount + 1):
            for coin in coins:
                new_total = total + coin
                if 0 < new_total < (amount + 1):
                    memo[new_total] = min(memo[new_total], 1 + memo[total])
        
        res = memo[amount]
        return res if res != math.inf else -1
        
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