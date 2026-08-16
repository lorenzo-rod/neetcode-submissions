class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2

        if target % 1 != 0:
            return False
        
        target = int(target)
        n = len(nums)
        memo = [False for _ in range(target*2 + 1)]
        memo[target] = True
        
        for i in reversed(range(n)):
            prev_memo = memo.copy()
            for total in reversed(range(target)):
                memo[total] = prev_memo[total + nums[i]] or prev_memo[total]

        return memo[0]
