import math
class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = 0

    def push(self, val: int) -> None:
        if not self.stack:
            self.minimum = val
            self.stack.append(0)
        else:
            diff = val - self.minimum
            self.minimum = val if diff < 0 else self.minimum
            self.stack.append(diff)

    def pop(self) -> None:
        diff = self.stack.pop()
        if diff < 0:
            self.minimum -= diff

    def top(self) -> int:
        return self.stack[-1] + self.minimum if self.stack[-1] >= 0 else self.minimum
        

    def getMin(self) -> int:
        return self.minimum
        
