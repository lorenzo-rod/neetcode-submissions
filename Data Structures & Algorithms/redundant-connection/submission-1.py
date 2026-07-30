class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i for i in range(len(edges) + 1)]
        rank = [1] * (n + 1)

        def find(node):
            
            while node != parents[node]:
                parents[node] = parents[parents[node]]
                node = parents[node]
            
            return node
        
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)

            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                parents[p2] = p1
                rank[p1] += rank[p2]
            else:
                parents[p1] = p2
                rank[p2] += 1
            
            return 1
        
        res = [0,0]
        for n1, n2 in edges:
            if not union(n1, n2):
                res = [n1, n2]
        
        return res