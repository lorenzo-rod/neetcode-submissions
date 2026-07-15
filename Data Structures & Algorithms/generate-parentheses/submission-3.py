class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(s, openings, closings):
            if len(s) == 2*n:
                res.append("".join(s))
                return
            if openings < n:
                s.append("(")
                backtrack(s, openings + 1, closings)
                s.pop()
            if closings < openings:
                s.append(")")
                backtrack(s, openings, closings + 1)
                s.pop()
        
        backtrack([], 0, 0)
        return res