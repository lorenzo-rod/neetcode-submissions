class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = [[0 for _ in range(2)] for _ in range(n+2)]

        for i in reversed(range(n)):
            for j in reversed(range(2)):

                if j == 1:
                    memo[i][j] = max(prices[i] + memo[i+2][0], memo[i+1][1])
                else:
                    memo[i][j] = max(memo[i+1][0], memo[i+1][1] - prices[i])
        
        return memo[0][0]

        def dfs(i, has_coin):
            if i >= n:
                return 0
            if (i, has_coin) in memo:
                return memo[(i, has_coin)]
            
            if has_coin:
                res = max(prices[i] + dfs(i+2, False), dfs(i+1, True))
            else:
                res = max(dfs(i+1, False), dfs(i+1, True) - prices[i])
            
            memo[(i, has_coin)] = res
            return res
        
        return dfs(0, False)
