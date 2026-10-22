import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append((t, v))

        heap = [(0, k)]
        maximum = 0
        explored = set()

        while heap:
            t1, node = heapq.heappop(heap)
            
            if node in explored:
                continue

            explored.add(node)
            maximum = t1

            for t2, nei in graph[node]:
                if nei not in explored:
                    heapq.heappush(heap, (t1 + t2, nei))
            
        
        return maximum if len(explored) == n else -1
