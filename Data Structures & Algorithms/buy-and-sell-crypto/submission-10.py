class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = 101
        res = 0

        for price in prices:
            minimum = min(minimum, price)
            res = max(res, price - minimum)

        return res
