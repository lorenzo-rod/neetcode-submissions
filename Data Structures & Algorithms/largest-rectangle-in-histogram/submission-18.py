class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        res = 0

        for i, h in enumerate(heights):
            idx = i
            while stack and stack[-1][1] > h:
                i, height = stack.pop()
                res = max(res, (idx - i) * height)
            stack.append((i, h))

        for i, h in stack:
            res = max(res, (len(heights) - i) * h)

        return res
        