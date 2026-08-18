class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = [0 for _ in range(2)]
        prev_1_1 = prev_2_0 = prev_1_0 = 0

        for i in reversed(range(n)):
            prev_2_0, prev_1_0, prev_1_1 = prev_1_0, memo[0], memo[1]
            memo[1] = max(prices[i] + prev_2_0, prev_1_1)
            memo[0] = max(prev_1_0, prev_1_1 - prices[i])
        
        return memo[0]
