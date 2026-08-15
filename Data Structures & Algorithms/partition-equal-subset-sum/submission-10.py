class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        n = len(nums)
        target = total // 2
        memo = {}

        for i in range(n+1):
            for j in range(total+1):
                memo[(i, j)] = False
        
        memo[(n, target)] = True

        for i in reversed(range(n)):
            for j in reversed(range(target)):
                memo[(i, j)] = memo[(i+1, j + nums[i])] or memo[(i+1, j)]
        
        return memo[(0, 0)]

        
        def dfs(i, total):
            if (i, total) in memo:
                return memo[(i, total)]
            
            memo[(i, total)] = dfs(i+1, total + nums[i]) or dfs(i+1, total)
            return memo[(i, total)]
        
        return dfs(0, 0)
            

