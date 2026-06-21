class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                for i in range(len(nums)):
                    nums[i] = abs(nums[i])
                return abs(num)
            nums[idx] *= - 1