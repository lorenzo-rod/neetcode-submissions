class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_keys = dict([num, i] for i, num in enumerate(nums))
        for i, num in enumerate(nums):
            reciprocal = target - num
            if reciprocal in num_keys and i != num_keys[reciprocal]:
                return [i, num_keys[reciprocal]]