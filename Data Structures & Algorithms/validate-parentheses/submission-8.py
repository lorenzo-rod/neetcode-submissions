class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map = {')' : '(', '}' : '{', ']' : '['}

        for c in s:
            if c in char_map:
                if not stack:
                    return False
                elif char_map[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        
        return not stack