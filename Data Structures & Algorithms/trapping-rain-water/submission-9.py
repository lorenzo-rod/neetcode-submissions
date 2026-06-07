class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        maxl = height[l]
        maxr = height[r]

        res = 0

        while l < r:
            if maxl < maxr:
                res += max(0, maxl - height[l])
                l += 1
                maxl = max(maxl, height[l])
            else:
                res += max(0, maxr - height[r])
                r -= 1
                maxr = max(maxr, height[r])
        return res