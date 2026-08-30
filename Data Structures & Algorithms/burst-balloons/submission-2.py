class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        memo = {}

        def dfs(nums):
            if tuple(nums) in memo:
                return memo[tuple(nums)]
            if not nums:
                return 0

            m = len(nums)
            res = 0
            
            for i in range(m):
                left = 1 if i == 0 else nums[i-1]
                right = 1 if i == m - 1 else nums[i+1]
                product = left * nums[i] * right
                res = max(res, product + dfs(nums[0:i] + nums[i+1:m]))
            
            memo[tuple(nums)] = res
            return res
        
        return dfs(nums)
