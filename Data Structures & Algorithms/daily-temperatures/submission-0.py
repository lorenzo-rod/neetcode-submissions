class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        temps = [(i, temperatures[i]) for i in range(len(temperatures))]
        res = [0] * len(temperatures)
        for i, temp in temps:
            while stack and stack[-1][1] < temp:
                index, _ = stack.pop()
                res[index] = i - index
            stack.append((i, temp))
        return res