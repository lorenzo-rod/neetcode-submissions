class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        signs = set(list(["+", "-", "*", "/"]))

        for s in tokens:

            if s in signs:

                b = stack.pop()
                a = stack.pop()
                res = 0

                if s == "+":
                    res = a + b
                elif s == "*":
                    res = a * b
                elif s == "-":
                    res = a - b
                else:
                    res = int(a / b)

                stack.append(res)
            else:
                stack.append(int(s))
        
        return stack[0]
