class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indexes = {}

        for i, num in enumerate(numbers):
            if target - num in indexes:
                return sorted([i + 1, indexes[target - num] + 1])
            indexes[num] = i
        
        return []