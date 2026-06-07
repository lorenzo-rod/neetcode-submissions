class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {(0, len(nums)): 1}

        def calcSumWays(target, idx):
            if (target, idx) in memo:
                return memo[(target, idx)]
            if idx == len(nums):
                memo[(target, idx)] = 0
                return memo[(target, idx)]
            memo[(target, idx)] = calcSumWays(
                target - nums[idx], idx + 1
            ) + calcSumWays(target + nums[idx], idx + 1)
            return memo[(target, idx)]

        return calcSumWays(target,0)
