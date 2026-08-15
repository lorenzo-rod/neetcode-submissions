class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        n = len(nums)
        target = total // 2
        memo = [[False for _ in range(total+1)] for _ in range(n+1)]
        memo[n][target] = True

        for i in reversed(range(n)):
            for j in reversed(range(target)):
                memo[i][j] = memo[i+1][j + nums[i]] or memo[i+1][j]
        
        return memo[0][0]
            