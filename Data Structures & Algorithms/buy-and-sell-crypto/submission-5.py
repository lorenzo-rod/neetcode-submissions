class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_found = prices[0]
        res = 0
        for price in prices:
            min_found = min(min_found, price)
            res = max(res, price - min_found)
        return res