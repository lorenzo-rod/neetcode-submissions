import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        data = [ -value for value in counter.values()]
        q = deque()
        steps = 0
        heapq.heapify(data)

        while data or q:
            steps += 1

            if data:
                cnt = 1 + heapq.heappop(data)
                if cnt != 0:
                    q.append((cnt, steps + n))
            
            if q and q[0][1] <= steps:
                heapq.heappush(data, q.popleft()[0])
        
        return steps