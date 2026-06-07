class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while(numbers[l] + numbers[r] != target):
            if target - numbers[l] - numbers[r] < 0:
                r -= 1
            if target - numbers[l] - numbers[r] > 0:
                l += 1
            print(l, r)
        return [l+1, r+1]