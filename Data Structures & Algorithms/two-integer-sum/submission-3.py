class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i
        for i, num in enumerate(nums):
            reciprocal = target - num
            if reciprocal in nums:
                j = nums_map[reciprocal]
                if i != j:
                    return [i, j]
