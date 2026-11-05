class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {']' : '[', ')' : '(', '}' : '{'}
        r_mapping = {value : key for key, value in mapping.items()}

        for c in s:
            if c in mapping:
                if not stack or mapping[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        
        return not stack
