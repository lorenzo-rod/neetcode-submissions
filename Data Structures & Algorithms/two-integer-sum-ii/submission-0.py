class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        num_sum = numbers[left] + numbers[right]
        while num_sum != target:
            if num_sum > target:
                right -= 1
            else:
                left += 1
            num_sum = numbers[left] + numbers[right]
        return [left+1, right+1]