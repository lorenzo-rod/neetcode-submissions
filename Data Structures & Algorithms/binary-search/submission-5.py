class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        
        return r if r < len(nums) and nums[r] == target else -1