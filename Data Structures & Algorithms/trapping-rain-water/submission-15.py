class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxl = [0] * n
        maxr = [0] * n
        water = [0] * n

        for i in range(1, n):
            maxl[i] = max(height[i-1], maxl[i-1])
        
        for i in reversed(range(n-1)):
            maxr[i] = max(height[i+1], maxr[i+1])

        for i in range(n):
            water[i] = max(min(maxl[i], maxr[i]) - height[i], 0)
        
        return sum(water)