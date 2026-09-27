from collections import defaultdict, deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        graph = defaultdict(list)
        n = len(nums)
        visited = set()

        for i, num in enumerate(nums):
            for j in range(1, num + 1):
                if i + j < n:
                    graph[i].append(i + j)
        
        q = deque([(0, 0)])
        visited.add(0)

        while q:
            node, jumps = q.popleft()

            if node == n - 1:
                return jumps
            
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, jumps + 1))
        