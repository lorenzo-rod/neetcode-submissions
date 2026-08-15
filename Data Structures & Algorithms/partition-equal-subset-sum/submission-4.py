class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}
        
        def dfs(i, total1, total2):
            if (i, total1) in memo:
                return memo[(i, total1)]
            if i == n:
                memo[(i, total1)] = total1 == total2
                return total1 == total2
            
            memo[(i, total1)] = dfs(i+1, total1 + nums[i], total2) or dfs(i+1, total1, total2 + nums[i])
            return memo[(i, total1)]
        
        return dfs(0, 0, 0)

