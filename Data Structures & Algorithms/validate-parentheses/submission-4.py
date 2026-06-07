class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {")" : "(", "]" : "[", "}" : "{"}
        for c in s:
            if c in bracket_map.values():
                stack.append(c)
            else:
                if not stack or bracket_map[c] != stack.pop():
                    return False
        return not stack