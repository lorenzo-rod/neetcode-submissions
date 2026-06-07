from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
        
        q = deque([i for i in range(numCourses) if not in_degree[i]])
        res = []
        
        while q:
            node = q.popleft()
            res.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        if len(res) == numCourses:
            return res
        
        return []