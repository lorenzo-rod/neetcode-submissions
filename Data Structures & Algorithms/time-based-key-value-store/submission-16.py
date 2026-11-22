from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        l, r = 0, len(self.values[key]) - 1

        while l <= r:
            m = (l + r) // 2
            v, t = self.values[key][m]

            if t <= timestamp:
                res = v
                l = m + 1
            else:
                r = m - 1
        
        return res
