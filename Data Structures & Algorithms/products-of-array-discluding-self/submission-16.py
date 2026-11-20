class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [1] * n

        for i in range(1, n):
            res[i] = nums[i-1] * res[i-1]
        
        suffix = 1

        for i in reversed(range(n-1)):
            suffix *= nums[i+1]
            res[i] = suffix * res[i]
        
        return res
