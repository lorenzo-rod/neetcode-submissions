import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = [(position[i], speed[i]) for i in range(n)]

        cars.sort()
        prev_steps = -1
        count = 0

        for pos, vel in reversed(cars):
            steps = (target - pos) / vel

            if steps > prev_steps:
                prev_steps = steps
                count += 1

        return count
