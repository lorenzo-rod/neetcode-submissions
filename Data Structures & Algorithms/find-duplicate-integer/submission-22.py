class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)

        for i in range(n):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                return idx + 1
            nums[idx] *= -1
