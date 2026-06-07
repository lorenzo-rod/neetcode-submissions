from collections import deque
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        int_map = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }

        str_map = {}

        for key, value in int_map.items():
            str_map[value] = key

        res = 0
        for i, c1 in enumerate(reversed(num1)):
            for j, c2 in enumerate(reversed(num2)):
                res += int_map[c1] * int_map[c2] * 10 ** (i + j)
        
        if res == 0:
            return "0"

        output = deque()

        while res:
            output.appendleft(str_map[res % 10])
            res //= 10

        return "".join(output)