class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, t in enumerate(temperatures):
            if not stack or stack[-1][1] >= t:
                stack.append((i, t))
            else:
                while stack and stack[-1][1] < t:
                    index, _ = stack.pop()
                    res[index] = i - index
                stack.append((i, t))

        return res
