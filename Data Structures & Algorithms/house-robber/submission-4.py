class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n < 3:
            return max(nums)

        dp = 0
        dp_2, dp_1 = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            dp = max(dp_1, dp_2 + nums[i])
            dp_2, dp_1 = dp_1, dp
        
        return dp