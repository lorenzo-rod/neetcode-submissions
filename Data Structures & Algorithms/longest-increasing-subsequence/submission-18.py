class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [0] * (n+1)
        
        for i in reversed(range(0, n)):
            for j in reversed((range(-1, i))):

                if j == -1 or nums[i] > nums[j]:
                    memo[j] = max(memo[j], 1 + memo[i])
        
        return memo[-1]