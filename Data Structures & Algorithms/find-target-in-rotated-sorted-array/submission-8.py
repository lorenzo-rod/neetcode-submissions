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

        i = self.binary_search(nums[0:pivot], target)
        j = self.binary_search(nums[pivot:len(nums)], target)

        if i != -1:
            return i
        
        if j != -1:
            return pivot + j
        
        return -1

    def binary_search(self, nums, target):
        if not nums:
            return -1

        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] < target:
                l = m + 1
            else:
                r = m

        return l if nums[l] == target else -1
