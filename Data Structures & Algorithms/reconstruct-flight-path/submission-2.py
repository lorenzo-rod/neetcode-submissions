from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(list)
        tickets.sort(reverse=True)

        for a, b in tickets:
            graph[a].append(b)

        path = []

        def dfs(node):
            while graph[node]:
                nei = graph[node].pop()
                dfs(nei)

            path.append(node)
        
        dfs("JFK")

        return list(reversed(path))
