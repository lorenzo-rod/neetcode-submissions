class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        total = 0
        res = nums[0]

        for num in nums:
            total = max(num, total + num)
            res = max(total, res)
        
        return res
