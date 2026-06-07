class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        row = [0,0]
        row_1 = [0,0]
        row_2 = [0,0]
        
        for i in reversed(range(len(prices))):
            row[0] = max(row_1[0], row_1[1] - prices[i])
            row[1] = max(row_1[1], row_2[0] + prices[i])
            row_2, row_1 = row_1[:], row[:]

        return row[0]
