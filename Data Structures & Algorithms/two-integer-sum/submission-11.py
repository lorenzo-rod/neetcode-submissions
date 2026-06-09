class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        keys = dict([[num, index] for index, num in enumerate(nums)])
        
        for i, num in enumerate(nums):
            if target - num in keys and i != keys[target - num]:
                return [i, keys[target - num]]
        
