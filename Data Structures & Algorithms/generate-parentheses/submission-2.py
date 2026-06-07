class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(path, openings, closings):
            if (len(path) == 2*n):
                res.append("".join(path))
                return
            if openings < n:
                path.append("(")
                backtrack(path, openings + 1, closings)
                path.pop()
            if closings < openings:
                path.append(")")
                backtrack(path, openings, closings + 1)
                path.pop()

        backtrack([], 0, 0)
        return res