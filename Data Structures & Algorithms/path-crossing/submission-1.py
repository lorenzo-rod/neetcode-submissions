class Solution:
    def isPathCrossing(self, path: str) -> bool:
        i, j = 0, 0
        visited = set()
        visited.add((i, j))
        for c in path:
            if c == "N":
                j += 1
            elif c == 'S':
                j -= 1
            elif c == 'E':
                i += 1
            else:
                i -= 1
            
            if (i, j) in visited:
                return True
            
            visited.add((i, j))
        
        return False