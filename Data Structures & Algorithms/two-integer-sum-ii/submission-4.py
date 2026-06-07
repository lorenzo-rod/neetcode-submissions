class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        sum_nums = numbers[l] + numbers[r]
        while(sum_nums != target):
            if target < sum_nums:
                r -= 1
            elif target > sum_nums:
                l += 1
            sum_nums = numbers[l] + numbers[r]
        return [l+1, r+1]