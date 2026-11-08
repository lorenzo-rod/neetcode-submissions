class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        pivot = l

        l, r = 0, pivot - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] < target:
                l = m + 1
            else:
                r = m

        if nums[l] == target:
            return l

        l, r = pivot, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] < target:
                l = m + 1
            else:
                r = m

        if nums[l] == target:
            return l
        
        return -1
