class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        minimum, maximum = 1,1
        for n in nums:
            if n == 0:
                maximum, minimum = 1, 1
                continue
            tmp = n * maximum
            maximum = max(n * maximum, n * minimum, n)
            minimum = min(tmp, n * minimum, n)
            res = max(res, maximum)
        return res