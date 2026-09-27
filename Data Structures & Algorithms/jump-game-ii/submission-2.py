import math
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = [math.inf] * (n)
        res[0] = 0

        for i, num in enumerate(nums):
            for j in range(num + 1):
                if i + j < n:
                    res[i + j] = min(res[i + j], res[i] + 1)
        
        return res[-1]