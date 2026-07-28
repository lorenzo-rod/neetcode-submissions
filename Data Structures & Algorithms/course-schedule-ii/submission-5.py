class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        res = []
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
        
        def dfs(node):
            res.append(node)
            in_degree[node] = -1
            
            for nei in graph[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    dfs(nei)
        
        for node in range(numCourses):
            if in_degree[node] == 0:
                dfs(node)
        
        return res if len(res) == numCourses else []