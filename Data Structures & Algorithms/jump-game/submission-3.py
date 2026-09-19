class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}
        
        def dfs(i):
            if i >= n - 1:
                return True
            if nums[i] == 0:
                return False
            if i in memo:
                return memo[i]
            
            for j in range(1, nums[i] + 1):
                if dfs(i + j):
                    memo[i] = True
                    return True
            
            memo[i] = False
            return False
        
        return dfs(0)
