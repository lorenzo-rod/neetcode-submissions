class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        n = len(nums)
        target = total // 2
        memo = {}
        
        def dfs(i, total):
            if (i, total) in memo:
                return memo[(i, total)]
            if i == n:
                if total == target:
                    return True
                return False
            
            memo[(i, total)] = dfs(i+1, total + nums[i]) or dfs(i+1, total)
            return memo[(i, total)]
        
        return dfs(0, 0)
            

