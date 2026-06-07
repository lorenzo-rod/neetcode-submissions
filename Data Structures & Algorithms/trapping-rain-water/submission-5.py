class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        n = len(height)
        maxl = [0] * n
        maxr = [0] * n
        res = 0

        for i in range(1, n):
            maxl[i] = max(height[i-1], maxl[i-1])
            maxr[n - i - 1] = max(height[n - i], maxr[n - i])


        for i in range(n):
            res += max(min(maxl[i], maxr[i]) - height[i], 0)
        
        return res