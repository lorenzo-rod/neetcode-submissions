class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)

        l, r = 0, n - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[-1]:
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

        l, r = pivot, n - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] < target:
                l = m + 1
            else:
                r = m
        
        return l if nums[l] == target else -1
        