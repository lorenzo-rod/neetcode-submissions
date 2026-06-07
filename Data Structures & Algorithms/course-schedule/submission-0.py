from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            graph[a].append(b)
            in_degree[b] += 1
        
        q = deque([i for i in range(numCourses) if not in_degree[i]])
        count = 0

        while q:
            node = q.popleft()
            count += 1
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        return count == numCourses

