class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[0 for _ in range(-1, n)] for _ in range(n+1)]
        
        for i in reversed(range(n)):
            for j in reversed(range(-1, n-1)):
                
                memo[i][j] = memo[i+1][j]

                if j == -1 or nums[i] > nums[j]:
                    memo[i][j] = max(memo[i][j], 1 + memo[i+1][i])
                
        return memo[0][-1]