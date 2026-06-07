class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        res[-1] = 1
        for i in reversed(range(n-1)):
            res[i] = res[i+1] * nums[i+1]
        left_product = 1
        for i in range(n):
            res[i] = left_product * res[i]
            left_product = left_product * nums[i]
        return res