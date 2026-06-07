class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        prev_steps = - 1
        res = 0
        for pos, vel in reversed(cars):
            steps = (target - pos) / vel
            if prev_steps < steps:
                res += 1
                prev_steps = steps
        return res