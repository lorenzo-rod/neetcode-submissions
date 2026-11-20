class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        idx = {}

        for i, n in enumerate(nums):
            idx[n] = i
        
        for i, num in enumerate(nums):
            reciprocal = target - num
            if reciprocal in idx:
                j = idx[reciprocal]
                if j != i:
                    return [i, j]
                    