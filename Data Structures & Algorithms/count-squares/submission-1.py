from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        for p1 in self.points:
            x = p1[0] - point[0]
            y = p1[1] - point[1]

            if abs(x) != abs(y) or x == 0 or y == 0:
                continue

            p2 = (point[0] + x, point[1])
            p3 = (point[0], point[1] + y)

            if p2 in self.points and p3 in self.points:
                res += self.points[p1] * self.points[p2] * self.points[p3]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
