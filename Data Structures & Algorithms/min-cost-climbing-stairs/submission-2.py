class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        res = res_1 = res_2 = 0

        for i in range(2, len(cost) + 1):
            res = min(res_1 + cost[i-1], res_2 + cost[i-2])
            res_2, res_1 = res_1, res
        
        return res