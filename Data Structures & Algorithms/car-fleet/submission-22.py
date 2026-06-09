class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        prev_steps = -1
        cars = sorted((zip(position, speed)))

        for pos, v in reversed(cars):
            steps = (target - pos) / v
            if prev_steps < steps:
                res += 1
                prev_steps = steps
        
        return res