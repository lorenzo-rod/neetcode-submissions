class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        signs = set(["+", "-", "*", "/"])
        for c in tokens:
            if c not in signs:
                stack.append(c)
            else:
                b = int(stack.pop())
                a = int(stack.pop())

                if c == "+":
                    stack.append(a + b)
                elif c == "-":
                    stack.append(a - b)
                elif c == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            
        return int(stack[-1])
