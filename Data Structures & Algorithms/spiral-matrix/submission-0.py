class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direction = directions[0]
        position = [0, 0]
        explored = set([(0, 0)])
        res = []
        m = len(matrix)
        n = len(matrix[0])
        k = 0

        while len(res) < m * n:
            res.append(matrix[position[0]][position[1]])
            if not (
                -1 < position[0] + direction[0] < m
                and -1 < position[1] + direction[1] < n
                and (position[0] + direction[0], position[1] + direction[1])
                not in explored
            ):
                k += 1
                k %= 4
                direction = directions[k]

            position[0] += direction[0]
            position[1] += direction[1]
            explored.add(tuple(position))

        return res
