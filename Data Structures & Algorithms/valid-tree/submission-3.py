from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen = set()
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node, prev):
            for neighbour in graph[node]:
                if neighbour != prev and neighbour in seen:
                    return False
                elif neighbour not in seen:
                    seen.add(neighbour)
                    if not dfs(neighbour, node):
                        return False
            return True
        
        seen.add(0)
        return dfs(0, -1) and len(seen) == n