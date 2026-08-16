class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2

        if target % 1 != 0:
            return False
        
        target = int(target)
        n = len(nums)
        memo = [[False for _ in range(target*2 + 1)] for _ in range(n+1)]
        for i in range(n+1):
            for total in range(target*2 + 1):
                if total == target:
                    memo[i][total] = True
        
        for i in reversed(range(n)):
            for total in reversed(range(target)):
                memo[i][total] = memo[i+1][total + nums[i]] or memo[i+1][total]

        return memo[0][0]
