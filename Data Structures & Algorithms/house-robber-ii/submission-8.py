class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n <= 3:
            return max(nums)

        dp = 0
        dp_2, dp_1 = nums[0], max(nums[0], nums[1])

        for i in range(2, n - 1):
            dp = max(dp_1, dp_2 + nums[i])
            dp_2, dp_1 = dp_1, dp
        
        res = dp
        dp = 0
        dp_2, dp_1 = nums[1], max(nums[1], nums[2])

        for i in range(3, n):
            dp = max(dp_1, dp_2 + nums[i])
            dp_2, dp_1 = dp_1, dp
        
        return max(res, dp)