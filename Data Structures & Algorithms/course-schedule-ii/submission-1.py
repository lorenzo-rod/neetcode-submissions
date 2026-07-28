from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        res = []
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
        
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])

        while q:
            node = q.popleft()
            res.append(node)

            for nei in graph[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
        
        return res if len(res) == numCourses else []