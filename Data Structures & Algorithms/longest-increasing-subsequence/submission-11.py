class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        for j in range(-1, n):
            memo[(n, j)] = 0
        
        for i in reversed(range(-1, n)):
            for j in reversed((range(-1, i))):
                memo[(i, j)] = memo[(i+1, j)]

                if j == -1 or nums[i] > nums[j]:
                    memo[(i, j)] = max(memo[(i, j)], 1 + memo[(i+1, i)])
        
        return memo[(0, -1)]