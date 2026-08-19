class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        memo = [0 for _ in range(amount + 1)]
        memo[amount] = 1

        for i in reversed(range(n)):
            prev_memo = memo.copy()
            for j in reversed(range(amount)):

                b = memo[j + coins[i]] if (j + coins[i]) <= amount else 0
                memo[j] = prev_memo[j] + b
        
        return memo[0]
            