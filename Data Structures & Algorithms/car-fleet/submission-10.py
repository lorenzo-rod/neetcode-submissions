class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(position[i], speed[i]) for i in range(len(position))])
        count = 0
        prev_steps = -1
        prev_vel = -1
        prev_pos = -1
        steps_arr = [0] * len(position)
        for i, (pos, vel) in enumerate(reversed(cars)):
            steps = (target - pos) / vel
            steps_arr[len(position) - i - 1] = steps if steps > prev_steps else prev_steps
            if steps > prev_steps:
                count += 1
                prev_steps = steps
        print(cars)
        print(steps_arr)
        return count