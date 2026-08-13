import math
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max, cur_min = 1, 1
        maximum = nums[0]

        for num in nums:
            tmp = cur_max * num
            cur_max = max(num * cur_min, num * cur_max, num)
            cur_min = min(tmp, num * cur_min, num)
            maximum = max(maximum, cur_max)
        
        return maximum