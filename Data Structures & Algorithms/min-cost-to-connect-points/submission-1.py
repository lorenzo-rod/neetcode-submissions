from collections import defaultdict
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for p1 in points:
            for p2 in points:
                if p1 != p2:
                    cost = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                    graph[(p1[0], p1[1])].append((cost, p2[0], p2[1]))
        
        heap = [(0, points[0][0], points[0][1])]
        explored = set()
        cost = 0

        while len(explored) != len(points):
            c, px, py = heapq.heappop(heap)

            if (px, py) in explored:
                continue
            
            explored.add((px, py))
            cost += c

            for nc, npx, npy in graph[(px, py)]:
                if (npx, npy) not in explored:
                    heapq.heappush(heap, (nc, npx, npy))
            
        return cost
        