from collections import deque
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

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

        str_map = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        n = len(num1) + len(num2)
        res = [0] * (n)
        for i, c1 in enumerate(reversed(num1)):
            for j, c2 in enumerate(reversed(num2)):
                res[n - 1 - i - j] += int_map[c1] * int_map[c2]
        
        for i in range(n-1, -1, -1):
            if res[i] > 9:
                res[i-1] += res[i] // 10
                res[i] %= 10
            res[i] = str_map[res[i]]
        
        start = 0
        while res[start] == "0":
            start += 1

        return "".join(res[start:])
        