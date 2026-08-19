class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        memo = [0 for _ in range(amount + 1)]
        memo[amount] = 1

        for i in reversed(range(n)):
            for j in reversed(range(amount)):

                if j + coins[i] <= amount:
                    b = memo[j + coins[i]]
                    memo[j] += b
        
        return memo[0]
            