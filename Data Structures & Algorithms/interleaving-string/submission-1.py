class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)

        if m + n != len(s3):
            return False
        
        if m == n == 0:
            return True

        grid = [[False] * (n + 1) for _ in range(m + 1)]
        
        for i in reversed(range(m)):
            if s3[i + n] == s1[i]:
                grid[i][n] = True
            else:
                break
        
        for j in reversed(range(n)):
            if s3[j + m] == s2[j]:
                grid[m][j] = True
            else:
                break

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if s3[i + j] == s1[i] and s3[i + j] == s2[j]:
                    grid[i][j] = grid[i + 1][j] or grid[i][j + 1]
                elif s3[i + j] == s1[i]:
                    grid[i][j] = grid[i + 1][j]
                elif s3[i + j] == s2[j]:
                    grid[i][j] = grid[i][j + 1]

        return grid[0][0]
