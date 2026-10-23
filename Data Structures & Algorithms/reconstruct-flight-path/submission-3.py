from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        tickets.sort(reverse=True)
        graph = defaultdict(list)

        for u, v in tickets:
            graph[u].append(v)

        path = []

        def dfs(node):

            while graph[node]:
                nei = graph[node].pop()
                dfs(nei)
            
            path.append(node)
        
        dfs("JFK")
        return list(reversed(path))
