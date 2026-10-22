import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append((t, v))

        heap = [(0, k)]
        maximum = 0
        explored = [0] * n
        count = 0

        while heap:
            t1, node = heapq.heappop(heap)
            
            if explored[node-1]:
                continue

            explored[node-1] = 1
            count += 1
            maximum = t1

            for t2, nei in graph[node]:
                if not explored[nei-1]:
                    heapq.heappush(heap, (t1 + t2, nei))
            
        
        return maximum if count == n else -1
