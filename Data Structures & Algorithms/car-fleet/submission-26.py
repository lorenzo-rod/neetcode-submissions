class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)

        cars = [(position[i], speed[i]) for i in range(n)]
        cars.sort()

        res = 0

        prev_steps = - 1
        steps = 0

        for pos, vel in reversed(cars):
            steps = (target - pos) / vel
            if prev_steps < steps:
                res += 1
                prev_steps = steps

        return res
