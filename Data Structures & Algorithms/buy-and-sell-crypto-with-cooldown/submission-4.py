class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = [0 for _ in range(2)]
        prev_1 = False

        for i in reversed(range(n)):
            prev_2 = prev_1.copy() if prev_1 else memo.copy()
            prev_1 = memo.copy()
            for j in reversed(range(2)):

                if j == 1:
                    memo[j] = max(prices[i] + prev_2[0], prev_1[1])
                else:
                    memo[j] = max(prev_1[0], prev_1[1] - prices[i])
        
        return memo[0]
