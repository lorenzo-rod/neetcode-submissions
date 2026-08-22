class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        n3 = len(s3)
        n1 = len(s1)
        n2 = len(s2)

        memo = {(n1, n2, n3) : True}
        
        def dfs(i, j, k):
            if (i, j, k) in memo:
                return memo[(i, j, k)]
            if k == n3:
                return False
            
            if i < n1 and s1[i] == s3[k]:
                if dfs(i+1, j, k+1):
                    memo[(i, j, k)] = True
                    return True

            if j < n2 and s2[j] == s3[k]:
                if dfs(i, j+1, k+1):
                    memo[(i, j, k)] = True
                    return True
            
            memo[(i, j, k)] = False
            return False
        
        return dfs(0, 0, 0)

