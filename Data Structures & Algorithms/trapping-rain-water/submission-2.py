class Solution:
    def trap(self, height: List[int]) -> int:
        trap_water = 0
        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]
        while(left < right):
            if max_left < max_right:
                trap_water += max(0, max_left - height[left])
                left += 1
                max_left = max(max_left, height[left])
            else:
                trap_water += max(0, max_right - height[right])
                right -= 1
                max_right = max(max_right, height[right])
        return trap_water