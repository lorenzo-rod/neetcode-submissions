class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}

        for i, num in enumerate(nums):
            indexes[num] = i
        
        for i, num in enumerate(nums):
            reciprocal = target - num
            if reciprocal in indexes:
                index = indexes[reciprocal]
                if index != i:
                    return [i, index]
        