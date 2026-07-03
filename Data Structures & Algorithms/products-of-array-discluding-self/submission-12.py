class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        res = [1] * n

        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]

        right_product = 1
        
        for i in reversed(range(n)):
            res[i] = res[i] * right_product
            right_product *= nums[i]
        
        return res