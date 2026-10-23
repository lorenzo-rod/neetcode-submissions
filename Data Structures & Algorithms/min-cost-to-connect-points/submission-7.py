import heapq
from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        n = len(points)

        for i in range(n):
            for j in range(i+1, n):
                p1 = tuple(points[i])
                p2 = tuple(points[j])
                cost = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                graph[p1].append((cost, p2[0], p2[1]))
                graph[p2].append((cost, p1[0], p1[1]))

        explored = set()
        heap = [(0, points[0][0], points[0][1])]
        cost = 0

        while len(explored) != n:

            c, nx, ny = heapq.heappop(heap)

            if (nx, ny) in explored:
                continue

            explored.add((nx, ny))
            cost += c

            for c1, nex, ney in graph[(nx, ny)]:
                if (nex, ney) not in explored:
                    heapq.heappush(heap, (c1, nex, ney))
            
        return cost
