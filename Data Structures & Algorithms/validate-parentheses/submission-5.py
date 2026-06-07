class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par_map = {')': '(', ']' : '[', '}': '{'}
        for c in s:
            if c in par_map:
                if not stack or par_map[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        return not stack