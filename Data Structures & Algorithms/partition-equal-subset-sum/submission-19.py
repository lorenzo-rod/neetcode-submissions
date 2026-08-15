class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        n = len(nums)
        target = total // 2
        memo = [False for _ in range(total+1)]
        memo[target] = True

        for i in reversed(range(n)):
            prev_memo = memo.copy()
            for j in reversed(range(target)):
                memo[j] = prev_memo[j + nums[i]] or prev_memo[j]
        
        return memo[0]
            