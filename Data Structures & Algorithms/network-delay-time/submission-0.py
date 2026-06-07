from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for time in times:
            graph[time[0]].append((time[1], time[2]))
        
        heap = [(0, k)]
        visited = set()
        max_time = 0

        while heap:
            node_time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            max_time = node_time
            for neighbor, time in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (node_time + time, neighbor))
        
        return max_time if len(visited) == n else -1