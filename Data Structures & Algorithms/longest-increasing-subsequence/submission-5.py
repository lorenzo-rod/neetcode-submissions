class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        print(n)
        memo = {}
        for j in range(-1, n+1):
            memo[(n, j)] = 0
        
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            res = dfs(i+1, j)

            if j == -1 or nums[i] > nums[j]:
                res = max(res, 1 + dfs(i+1, i))
            
            memo[(i, j)] = res
            return res
        
        return dfs(0, -1)
            

            

