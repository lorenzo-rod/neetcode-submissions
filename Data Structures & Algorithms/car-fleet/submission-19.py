class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        prev_steps = -1
        count = 0
        for pos, vel in cars:
            steps = (target - pos) / vel
            if prev_steps < steps:
                count += 1
                prev_steps = steps
        return count
        