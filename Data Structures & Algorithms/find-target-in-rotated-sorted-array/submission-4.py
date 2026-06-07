class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        minimum = right

        while(left < right):
            if (nums[left] < nums[right]):
                minimum = left if nums[left] < nums[minimum] else minimum
                break
            mid = (left + right) // 2
            minimum = mid if nums[mid] < nums[minimum] else minimum
            if (nums[left] < nums[mid]):
                left = mid + 1
            else:
                right = mid

        def binarySearch(numbers, target):
            if not numbers:
                return -1
            left = 0
            right = len(numbers) - 1
            while(left < right):
                mid = (left + right) // 2
                if (numbers[mid] < target):
                    left = mid + 1
                else:
                    right = mid
            return left if numbers[left] == target else -1
        
        if minimum == len(nums) - 1:
            maximum = 0
        elif minimum == 0:
            maximum = len(nums) - 1
        else:
            maximum = minimum - 1
        
        if target >= nums[minimum] and target <= nums[-1]:
            a = binarySearch(nums[minimum:], target)
            return a + minimum if a != -1 else a
        elif target >= nums[0] and target <= nums[maximum]:
            return binarySearch(nums[:minimum], target)
        
        return -1
        