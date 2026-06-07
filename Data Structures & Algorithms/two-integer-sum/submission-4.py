class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = dict([(num, index) for index, num in enumerate(nums)])
        for i in range(len(nums)):
            reciprocal = target - nums[i]
            if reciprocal in nums_map:
                if nums_map[reciprocal] != i:
                    return [i, nums_map[reciprocal]]
