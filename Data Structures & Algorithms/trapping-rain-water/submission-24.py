class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxl, maxr = height[0], height[-1]
        l, r =  1, len(height) - 2
        res = 0

        while l <= r:
            if maxl < maxr:
                res += max(maxl - height[l], 0)
                maxl = max(maxl, height[l])
                l += 1
            else:
                res += max(maxr - height[r], 0)
                maxr = max(maxr, height[r])
                r -= 1
        
        return res