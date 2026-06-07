class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        rank = [1] * n

        def find(node):

            while parents[node] != node:
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
                rank[p2] += rank[p1]

            return 1
        
        res = n
        for n1, n2 in edges:
            res -= union(n1,n2)
        
        return res