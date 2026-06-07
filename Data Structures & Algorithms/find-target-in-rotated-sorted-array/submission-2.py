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
        print(minimum)
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
            print(numbers[left])
            return left if numbers[left] == target else -1
        
        a = binarySearch(nums[:minimum], target)
        b = binarySearch(nums[minimum:], target)

        if a != -1:
            return a
        elif b != -1:
            return b + minimum
        return -1
        
        