class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)

        if m + n != len(s3):
            return False
        
        grid = {(m, n) : True}

        def calcInterLeave(i, j):
            if (i, j) in grid:
                return grid[(i,j)]

            if i < m and j < n and s3[i + j] == s1[i] and s3[i + j] == s2[j]:
                grid[(i,j)] = calcInterLeave(i + 1, j) or calcInterLeave(i, j + 1)
            elif i < m and s3[i + j] == s1[i]:
                grid[(i,j)] = calcInterLeave(i + 1, j)
            elif j < n and s3[i + j] == s2[j]:
                grid[(i,j)] = calcInterLeave(i, j + 1)
            else:
                grid[(i,j)] = False
            
            return grid[(i,j)]

        return calcInterLeave(0, 0)
