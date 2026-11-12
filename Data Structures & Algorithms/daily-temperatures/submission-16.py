class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        stack = []
        res = [0] * n

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                idx, _ = stack.pop()
                res[idx] = i - idx
            stack.append((i, t))
        
        return res
        