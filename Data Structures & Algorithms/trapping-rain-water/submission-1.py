class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_heights = [0] * n
        right_heights = [0] * n
        trap_water = 0
        for i in range(1, n):
            left_heights[i] = max(left_heights[i-1], height[i-1])
        for i in reversed(range(n - 1)):
            right_heights[i] = max(right_heights[i+1], height[i+1])
        for i in range(1, n - 1):
            trap_water += max(min(left_heights[i], right_heights[i]) - height[i], 0)
        return trap_water