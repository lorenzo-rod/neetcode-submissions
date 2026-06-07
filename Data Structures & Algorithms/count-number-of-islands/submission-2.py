from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def bfs(node):
            q = deque([node])
            grid[node[0]][node[1]] = "0"
            while q:
                node = q.popleft()
                for dir_x, dir_y in directions:
                    new_node = (node[0] + dir_x, node[1] + dir_y)
                    if (
                        (-1 < new_node[0] < m)
                        and (-1 < new_node[1] < n)
                        and grid[new_node[0]][new_node[1]] == "1"
                    ):
                        q.append(new_node)
                        grid[new_node[0]][new_node[1]] = "0"

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    bfs((i, j))

        return count