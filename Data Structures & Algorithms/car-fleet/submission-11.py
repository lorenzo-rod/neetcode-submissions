class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(position[i], speed[i]) for i in range(len(position))])
        count = 0
        prev_steps = -1
        for pos, vel in reversed(cars):
            steps = (target - pos) / vel
            if steps > prev_steps:
                count += 1
                prev_steps = steps
        return count