class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right_products = [0] * n
        right_products[n-1] = 1
        left_products = [0] * n
        left_products[0] = 1
        res = [0] * n
        for i in reversed(range(n-1)):
            right_products[i] = right_products[i+1] * nums[i+1]
        for i in range(1, n):
            left_products[i] = left_products[i-1] * nums[i-1]
        res = [left_products[i] * right_products[i] for i in range(n)]
        return res