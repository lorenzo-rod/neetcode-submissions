class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        memo = [[0 for _ in range(amount + 1)] for _ in range(n+1)]
        for i in range(n+1):
            memo[i][amount] = 1

        for i in reversed(range(n)):
            for j in reversed(range(amount)):

                b = memo[i][j + coins[i]] if (j + coins[i]) <= amount else 0
                memo[i][j] = memo[i+1][j] + b
        
        return memo[0][0]

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
            