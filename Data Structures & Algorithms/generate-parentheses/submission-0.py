class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(path, score):
            if (score < 0):
                return
            if (len(path) == 2*n):
                if score == 0:
                    res.append("".join(path))
                return
            for c in [("(",1), (")",-1)]:
                path.append(c[0])
                backtrack(path, score + c[1])
                path.pop()
        backtrack([], 0)
        return res