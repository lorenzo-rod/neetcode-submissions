from collections import defaultdict, deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        explored = [0] * n

        def bfs(node):
            q = deque([node])
            explored[node] = 1
            while q:
                node = q.popleft()
                for neighbor in graph[node]:
                    if not explored[neighbor]:
                        explored[neighbor] = 1
                        q.append(neighbor)
        
        count = 0

        for node in range(n):
            if not explored[node]:
                bfs(node)
                count += 1
        
        return count
