class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minimum = nums[-1]
        while (left < right):
            if (nums[left] < nums[right]):
                minimum = min(nums[left], minimum)
                break
            mid = (left + right) // 2
            minimum = min(minimum, nums[mid])
            if (nums[left] < nums[mid]):
                left = mid + 1
            else:
                right = mid
        return minimum