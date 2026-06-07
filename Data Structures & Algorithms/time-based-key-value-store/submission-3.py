from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        values = self.data[key]
        left = 0
        right = len(values)
        while (left < right):
            mid = (left + right) // 2
            if (values[mid][1] < timestamp):
                left = mid + 1
            else:
                right = mid
        if left == len(values):
            return values[-1][0]
        if left == 0:
            return values[0][0] if values[0][1] == timestamp else ""
        return values[left][0] if values[left][1] == timestamp else values[left-1][0]
