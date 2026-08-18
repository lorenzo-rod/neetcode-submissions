class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}

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
