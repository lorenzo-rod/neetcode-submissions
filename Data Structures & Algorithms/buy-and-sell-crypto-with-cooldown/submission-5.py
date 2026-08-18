class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = [0 for _ in range(2)]
        prev_1_1 = 0
        prev_2_0 = 0
        prev_1_0 = 0

        for i in reversed(range(n)):
            prev_2_0 = prev_1_0
            prev_1_0 = memo[0]
            prev_1_1 = memo[1]
            for j in reversed(range(2)):

                if j == 1:
                    memo[j] = max(prices[i] + prev_2_0, prev_1_1)
                else:
                    memo[j] = max(prev_1_0, prev_1_1 - prices[i])
        
        return memo[0]
