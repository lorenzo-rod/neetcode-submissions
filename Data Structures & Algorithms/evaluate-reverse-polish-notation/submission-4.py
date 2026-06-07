import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            print(stack)
            if c.isdigit():
                stack.append(int(c))
            elif c[1:].isdigit():
                stack.append(- int(c[1:]))
            else:
                if c == "+":
                    result = stack[-2] + stack[-1]
                elif c == "-":
                    result = stack[-2] - stack[-1]
                elif c == "*":
                    result = stack[-2] * stack[-1]
                elif c == "/":
                    result = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(result)
        return stack[-1]