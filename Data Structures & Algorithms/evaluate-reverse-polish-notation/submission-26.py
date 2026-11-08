class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if len(c) > 1 or ord('0') <= ord(c) <= ord('9'):
                stack.append(c)
            else:
                b = int(stack.pop())
                a = int(stack.pop())

                if c == "+":
                    stack.append(str(a + b))
                elif c == '-':
                    stack.append(str(a - b))
                elif c == '*':
                    stack.append(str(a * b))
                else:
                    stack.append(str(int(a / b)))
                
        return int(stack.pop())
