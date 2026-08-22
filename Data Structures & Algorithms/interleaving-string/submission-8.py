class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        if n1 + n2 != n3:
            return False

        memo = {(n1, n2) : True}
        
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            k = i + j

            if i < n1 and s1[i] == s3[k]:
                if dfs(i+1, j):
                    memo[(i, j)] = True
                    return True

            if j < n2 and s2[j] == s3[k]:
                if dfs(i, j+1):
                    memo[(i, j)] = True
                    return True
            
            memo[(i, j)] = False
            return False
        
        return dfs(0, 0)

