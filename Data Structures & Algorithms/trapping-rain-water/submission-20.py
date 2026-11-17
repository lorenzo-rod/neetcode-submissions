class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        maxl = [0] * n
        maxr = [0] * n
        res = 0

        for i in range(1, n):
            maxl[i] = max(maxl[i-1], height[i-1])
        
        for i in reversed(range(n - 1)):
            maxr[i] = max(maxr[i+1], height[i+1])

        for i in range(n):
            res += max(0, min(maxl[i], maxr[i]) - height[i])

        return res
