class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        m = amount + 1

        row = [0] * m
        row[-1] = 1

        for i in reversed(range(len(coins))):
            for j in reversed(range(m - 1)):
                row[j] = row[j] + row[j + coins[i]] if j + coins[i] < m else row[j]

        return row[0]
