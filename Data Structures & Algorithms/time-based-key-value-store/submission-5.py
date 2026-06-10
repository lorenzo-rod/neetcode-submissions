from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.values:
            return ""

        value_list = self.values[key]
        l = 0
        r = len(value_list)

        while l < r:
            m = (l + r) // 2
            if value_list[m][0] < timestamp:
                l = m + 1
            else:
                r = m
        
        if l == len(value_list):
            return value_list[-1][1]
        
        if l == 0 and value_list[l][0] != timestamp:
            return ""

        return value_list[l][1] if value_list[l][0] == timestamp else value_list[l-1][1]





