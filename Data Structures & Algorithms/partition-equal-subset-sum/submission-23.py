class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2

        if target % 1 != 0:
            return False
        
        target = int(target)
        n = len(nums)
        memo = {}
        for i in range(n+1):
            memo[(i, target)] = True
        for total in range(target*2 + 1):
            memo[(n, total)] = False
        
        def dfs(i, total):
            if (i, total) in memo:
                return memo[(i, total)]
            
            memo[(i, total)] = dfs(i+1, total + nums[i]) or dfs(i+1, total)
            return memo[(i, total)]
        
        return dfs(0, 0)
