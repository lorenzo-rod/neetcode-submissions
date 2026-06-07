class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minimum = nums[0]
        while (left <= right):
            if (nums[left] < nums[right]):
                minimum = min(minimum, nums[left])
                break
            mid = (left + right) // 2
            minimum = min(nums[mid], minimum)
            if (nums[left] <= nums[mid]):
                left = mid + 1
            else:
                right = mid
        return minimum