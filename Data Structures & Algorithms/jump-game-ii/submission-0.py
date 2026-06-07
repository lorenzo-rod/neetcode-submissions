class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [n+1] * n
        dp[0] = 0

        for i in range(n):
            for j in range(nums[i]):
                if i + j + 1 < n and dp[i+j+1] == n + 1:
                    dp[i+j+1] = min(dp[i] + 1, dp[i+j+1])
                    if i + j + 1 == n - 1:
                        return dp[-1]

        return dp[-1]