class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        n = len(nums)
        target = total // 2
        memo = [False for _ in range(total+1)]
        memo[target] = True
        prev_memo = memo.copy()

        for i in reversed(range(n)):
            for j in reversed(range(target)):
                memo[j] = prev_memo[j + nums[i]] or prev_memo[j]
            prev_memo = memo.copy()
        
        return memo[0]
            