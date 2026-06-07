class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c.isdigit():
                stack.append(int(c))
            elif c[1:].isdigit():
                stack.append(-int(c[1:]))
            else:
                b = stack.pop()
                a = stack.pop()
                if c == "+":
                    stack.append(a + b)
                elif c == "-":
                    stack.append(a - b)
                elif c == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
        return stack[-1]