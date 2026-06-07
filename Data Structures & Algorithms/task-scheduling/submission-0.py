import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        data = [- value for value in count.values()]
        heapq.heapify(data)
        q = deque()
        steps = 0
        while data or q:
            steps += 1
            if data:
                cnt = 1 + heapq.heappop(data)
                if cnt:
                    q.append((cnt, steps + n))
            if q and q[0][1] <= steps:
                heapq.heappush(data, q.popleft()[0])
        return steps