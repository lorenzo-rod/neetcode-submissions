class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indexes = dict([value, index] for index, value in enumerate(numbers))

        for i, num in enumerate(numbers):
            if target - num in indexes:
                return sorted([i + 1, indexes[target - num] + 1])
        
        return []