class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = dict([num, index] for index, num in enumerate(nums))
        for i, num in enumerate(nums):
            reciprocal = target - num
            if reciprocal in nums_map and i != nums_map[reciprocal]:
                return [i, nums_map[reciprocal]]