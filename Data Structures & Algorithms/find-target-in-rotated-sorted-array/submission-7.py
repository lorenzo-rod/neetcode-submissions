class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        pivot = l

        if target > nums[pivot - 1] or target < nums[pivot]:
            return -1

        if target <= nums[-1] and target >= nums[pivot]:
            l = pivot
            r = len(nums) - 1
        else:
            l = 0
            r = pivot - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        
        return l if nums[l] == target else -1

