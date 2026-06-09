class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for i, height in enumerate(heights):
            index = i
            while stack and stack[-1][1] > height:
                index, h = stack.pop()
                res = max(res, h * (i - index))
            stack.append((index, height))
        for i, h in stack:
            res = max(res, (len(heights) - i) * h)
        return res