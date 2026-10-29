from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:

        count = 0
    
        for p in self.points:
            dx, dy = p[0] - point[0], p[1] - point[1]

            if dx != 0 and abs(dx) == abs(dy):
                p1 = (p[0] - dx, p[1])
                p2 = (p[0], p[1] - dy)

                if p1 in self.points and p2 in self.points:
                    count += self.points[p] * self.points[p1] * self.points[p2]
        
        return count

