class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {num : i for i, num in enumerate(nums)}

        for i, num in enumerate(nums):
            reciprocal = target - num
            if reciprocal in indexes and indexes[reciprocal] != i:
                return [i, indexes[reciprocal]]
        
