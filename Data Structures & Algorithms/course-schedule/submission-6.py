class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        count = 0

        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
        
        def dfs(node):
            nonlocal count
            count += 1
            in_degree[node] = -1

            for nei in graph[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    dfs(nei)
        
        for node in range(numCourses):
            if in_degree[node] == 0:
                dfs(node)
        
        
        return count == numCourses