import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = - math.inf
        res = - math.inf

        for num in nums:
            if num > total + num:
                total = num
            else:
                total += num
            res = max(res, total)
        
        return res
