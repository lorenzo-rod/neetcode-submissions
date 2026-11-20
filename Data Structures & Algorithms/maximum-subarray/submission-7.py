class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        total = nums[0]
        res = nums[0]

        for num in nums[1:]:
            total = max(num, total + num)
            res = max(total, res)
        
        return res
