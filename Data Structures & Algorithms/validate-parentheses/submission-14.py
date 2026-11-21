class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map = { ')' : '(', ']' : '[', '}' : '{'}

        for c in s:
            if c not in char_map:
                stack.append(c)
            else:
                if not stack or stack.pop() != char_map[c]:
                    return False
        
        return not stack
