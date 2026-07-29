class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [0] * n
        
        def dfs(node):
            if visited[node] == 1:
                return
            
            visited[node] = 1

            for nei in graph[node]:
                dfs(nei)

        res = 0
        
        for node in range(n):
            if visited[node] == 0:
                dfs(node)
                res += 1
        
        return res