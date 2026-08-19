class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        memo = {}

        def dfs(i, total):
            if (i, total) in memo:
                return memo[(i, total)]
            if total == amount:
                return 1
            if i == n or total > amount:
                return 0
            
            res = dfs(i+1, total) + dfs(i, total + coins[i])
            memo[(i, total)] = res
            return res
        
        return dfs(0, 0)
            