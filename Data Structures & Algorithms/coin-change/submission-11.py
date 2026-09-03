import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = {}

        def dfs(i, total):
            if total == amount:
                return 0
            if i == n:
                return math.inf
            if total > amount:
                return math.inf
            if (i, total) in memo:
                return memo[(i, total)]
            
            memo[(i, total)] = min(1 + dfs(i, total + coins[i]), dfs(i+1, total))
            return memo[(i, total)]
        
        res = dfs(0, 0)
        return res if res != math.inf else -1
        
