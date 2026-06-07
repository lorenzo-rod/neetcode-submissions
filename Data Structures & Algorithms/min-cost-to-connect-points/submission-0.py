from collections import defaultdict
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = defaultdict(list)
        res = 0

        for u in range(n):
            for v in range(u + 1, n):
                w = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                graph[u].append((v, w))
                graph[v].append((u, w))
        
        heap = [(0, 0)]
        explored = set()

        while heap:
            cost, u = heapq.heappop(heap)
            if u in explored:
                continue
            explored.add(u)
            res += cost
            for v, w in graph[u]:
                if v not in explored:
                    heapq.heappush(heap, (w, v))

        return res
