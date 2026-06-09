class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m
        
        min_index = l

        if target < nums[min_index] or target > nums[min_index - 1]:
            return -1
        
        if target <= nums[-1]:
            l = min_index
            r = len(nums) - 1
        else:
            l = 0
            r = min_index - 1
        

        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m

        return l if nums[l] == target else -1
