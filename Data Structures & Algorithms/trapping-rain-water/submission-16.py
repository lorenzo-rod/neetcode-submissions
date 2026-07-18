class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxl = height[0]
        maxr = height[-1]
        l, r =  1, len(height) - 2
        water = [0] * n

        while l <= r:
            if maxl < maxr:
                water[l] = max(maxl - height[l], 0)
                maxl = max(maxl, height[l])
                l += 1
            else:
                water[r] = max(maxr - height[r], 0)
                maxr = max(maxr, height[r])
                r -= 1
        
        return sum(water)