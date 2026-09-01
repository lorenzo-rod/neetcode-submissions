class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m = len(coins)
        memo = [0 for _ in range(amount+1)]
        memo[amount] = 1
        
        for i in reversed(range(m)):
            prev = memo.copy()
            for j in reversed(range(amount)):

                memo[j] = prev[j]

                if j + coins[i] <= amount:
                    memo[j] += memo[j + coins[i]]
        
        return memo[0]
