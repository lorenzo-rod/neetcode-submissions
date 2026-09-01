class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m = len(coins)
        memo = [0 for _ in range(amount+1)]
        memo[amount] = 1
        
        for i in reversed(range(m)):
            for j in reversed(range(amount)):

                if j + coins[i] <= amount:
                    memo[j] += memo[j + coins[i]]
        
        return memo[0]
