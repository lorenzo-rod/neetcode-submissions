class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        total = nums[0]
        res = nums[0]

        for num in nums[1:]:
            if total < 0:
                total = num
            else:
                total += num
            res = max(total, res)
        
        return res
