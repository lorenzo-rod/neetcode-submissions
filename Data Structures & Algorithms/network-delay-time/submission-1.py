from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append((t, v))
        
        delaytime = {}
        heap = [(0, k)]
        maximum = 0

        while heap:
            w1, n1 = heapq.heappop(heap)

            if n1 in delaytime:
                continue
            
            delaytime[n1] = w1
            maximum = w1

            for w2, n2 in graph[n1]:
                if n2 not in delaytime:
                    heapq.heappush(heap, (w1 + w2, n2))
            
        return maximum if len(delaytime) == n else -1
