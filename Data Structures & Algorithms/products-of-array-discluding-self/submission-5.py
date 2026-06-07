class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        res[0] = 1
        res[n - 1] = 1
        left_product = 1

        for i in reversed(range(n - 1)):
            res[i] = res[i+1] * nums[i+1]

        for i in range(1, n):
            left_product = left_product * nums[i-1]
            res[i] = left_product * res[i]

        return res