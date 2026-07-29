from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False

        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()

        q = deque([(0, -1)])

        while q:
            node, parent = q.popleft()

            if node in visited:
                return False
            
            for nei in graph[node]:
                if nei != parent:
                    q.append((nei, node))

            visited.add(node)
        
        return len(visited) == n