class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0])
        t, d = 0, len(matrix)
        res = []

        while l < r and t < d:
            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1
            for i in range(t, d):
                res.append(matrix[i][r-1])
            r -= 1
            if not ( l < r and t < d):
                break
            for i in reversed(range(l, r)):
                res.append(matrix[d-1][i])
            d -= 1
            for i in reversed(range(t, d)):
                res.append(matrix[i][l])
            l += 1
        
        return res
