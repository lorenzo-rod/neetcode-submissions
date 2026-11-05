class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        product = [1] * n

        for i in reversed(range(n-1)):
            product[i] = product[i+1] * nums[i+1]

        suffix = 1
        for i in range(n):
            product[i] = product[i] * suffix
            suffix *= nums[i]
        
        return product
