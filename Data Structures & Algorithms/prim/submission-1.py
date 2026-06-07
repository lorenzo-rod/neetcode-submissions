from collections import defaultdict
import heapq
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        heap = [(0, 0)]
        explored = set()

        while heap:
            cost, node = heapq.heappop(heap)
            if node in explored:
                continue
            explored.add(node)
            res += cost
            for v, w in graph[node]:
                if v not in explored:
                    heapq.heappush(heap, (w, v))
            
        return res if len(explored) == n else -1
