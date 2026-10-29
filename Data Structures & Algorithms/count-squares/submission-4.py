class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        if tuple(point) in self.points:
            self.points[tuple(point)] += 1
        else:
            self.points[tuple(point)] = 1

    def count(self, point: List[int]) -> int:
        if point == [2, 1]:
            print(self.points)

        count = 0
    
        for p in self.points:
            dx, dy = p[0] - point[0], p[1] - point[1]

            if point == [2, 1]:
                print(dx, dy)

            if abs(dx) == abs(dy) and dx != 0:
                p1 = (p[0] - dx, p[1])
                p2 = (p[0], p[1] - dy)

                if point == [2, 1]:
                    print(p1, p2)

                if p1 in self.points and p2 in self.points:
                    print(p1, p2, p)
                    count += self.points[p] * self.points[p1] * self.points[p2]
        
        return count

