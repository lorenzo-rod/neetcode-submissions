class Solution:
    def isValid(self, s: str) -> bool:
        mapping = { ')' : '(', ']' : '[', '}' : '{'}
        stack = []

        for c in s:
            if c not in mapping:
                stack.append(c)
            elif not stack or mapping[c] != stack.pop():
                return False

        return not stack
        