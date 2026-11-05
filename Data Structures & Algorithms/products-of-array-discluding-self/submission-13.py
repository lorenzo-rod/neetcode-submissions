class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        right_product = [1] * n
        left_product = [1] * n

        for i in reversed(range(n-1)):
            right_product[i] = right_product[i+1] * nums[i+1]

        for i in range(1, n):
            left_product[i] = left_product[i-1] * nums[i-1]
        
        return [left_product[i] * right_product[i] for i in range(n)]
        