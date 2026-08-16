class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [0 for _ in range(-1, n)]
        
        for i in reversed(range(n)):
            prev_memo = memo.copy()
            for j in reversed(range(-1, n-1)):
                
                memo[j] = prev_memo[j]

                if j == -1 or nums[i] > nums[j]:
                    memo[j] = max(memo[j], 1 + prev_memo[i])
                
        return memo[-1]