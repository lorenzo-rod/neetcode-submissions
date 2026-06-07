from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        land = []
        seen = set()
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    land.append((i,j))
        
        def bfs(node):
            q = deque([node])
            while q:
                node = q.popleft()
                seen.add(node)
                for dir_x, dir_y in [[0,1], [1,0], [0,-1], [-1,0]]:
                    new_node = (node[0] + dir_x, node[1] + dir_y)
                    if (-1 < new_node[0] < m) and (-1 < new_node[1] < n):
                        if grid[new_node[0]][new_node[1]] == "1" and new_node not in seen:
                            q.append(new_node)

        count = 0
        for node in land:
            if node not in seen:
                count += 1
                bfs(node)

        return count  