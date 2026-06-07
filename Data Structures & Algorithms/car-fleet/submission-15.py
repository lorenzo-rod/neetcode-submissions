class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(position[i], speed[i]) for i in range(len(position))], reverse=True)
        stack = []
        for pos, vel in cars:
            stack.append((target - pos) / vel)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)