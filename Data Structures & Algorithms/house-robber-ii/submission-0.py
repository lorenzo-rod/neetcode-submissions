class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]

        c0, c1, c2 = 0, 0, 0
        for i in reversed(range(1, n)):
            c0 = max(nums[i] + c2, c1)
            c2, c1 = c1, c0
        
        a0, a1, a2 = 0, 0, 0
        for i in reversed(range(n-1)):
            a0 = max(nums[i] + a2, a1)
            a2, a1 = a1, a0

        return max(c0, a0)