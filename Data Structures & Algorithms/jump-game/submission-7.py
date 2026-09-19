class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        start = n - 1

        for i in reversed(range(n)):
            if nums[i] + i >= start:
                start = i
        
        return start == 0
