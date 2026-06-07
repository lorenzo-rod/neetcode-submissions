class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        max_l = height[l]
        max_r = height[r]
        while l < r:
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                water = min(max_l, max_r) - height[l]
                res += water if water > 0 else 0
            else:
                r -= 1
                max_r = max(max_r, height[r])
                water = min(max_l, max_r) - height[r]
                res += water if water > 0 else 0
        return res