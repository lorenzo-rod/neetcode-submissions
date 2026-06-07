class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {")" : "(", "]" : "[", "}" : "{"}
        for c in s:
            if c in bracket_map.values():
                stack.append(c)
            elif c in bracket_map:
                if not stack or stack.pop() != bracket_map[c]:
                    return False
        return not stack