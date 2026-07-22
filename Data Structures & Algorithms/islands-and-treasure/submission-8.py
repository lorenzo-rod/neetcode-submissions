from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        treasures = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    treasures.append((i, j))
        
        q = deque(treasures)
        visited = set()

        print(grid)

        while q:
            i, j = q.popleft()
            for dx, dy in directions:
                neighbor = (i + dx, j + dy)
                if ((neighbor not in visited) 
                and (-1 < neighbor[0] < len(grid))
                and (-1 < neighbor[1] < len(grid[0]))
                and (grid[neighbor[0]][neighbor[1]]) > 0):
                    q.append(neighbor)
                    visited.add(neighbor)
                    grid[neighbor[0]][neighbor[1]] = grid[i][j] + 1
        

