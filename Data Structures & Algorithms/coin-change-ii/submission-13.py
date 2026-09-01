class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m = len(coins)
        memo = [[0 for _ in range(amount+1)] for _ in range(m+1)]

        for i in range(m+1):
            memo[i][amount] = 1
        
        for i in reversed(range(m)):
            for j in reversed(range(amount)):

                memo[i][j] = memo[i+1][j]

                if j + coins[i] <= amount:
                    memo[i][j] += memo[i][j + coins[i]]
        
        return memo[0][0]


        memo = {}
        
        def dfs(i, total):
            if total > amount:
                return 0
            if total == amount:
                return 1
            if i == m:
                return 0
            if (i, total) in memo:
                return memo[(i, total)]
            
            memo[(i, total)] = dfs(i, total + coins[i]) + dfs(i+1, total)
            return memo[(i, total)]
        
        return dfs(0, 0)