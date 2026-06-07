class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixes = [1] * n
        res = [1] * n
        for i in range(1, n):
            prefixes[i] = prefixes[i-1] * nums[i-1]
        suffix = 1
        for i in reversed(range(n)):
            res[i] = suffix * prefixes[i]
            suffix *= nums[i]
        return res