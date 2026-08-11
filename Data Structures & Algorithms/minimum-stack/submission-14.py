class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = 0

    def push(self, val: int) -> None:
        if not self.stack:
            self.minimum = val
            diff = 0
        else:
            diff = val - self.minimum
            self.minimum = val if diff < 0 else self.minimum
        self.stack.append(diff)

    def pop(self) -> None:
        diff = self.stack.pop()
        if diff < 0:
            self.minimum -= diff
            
    def top(self) -> int:
        diff = self.stack[-1]
        if diff < 0:
            return self.minimum
        return self.minimum + diff

    def getMin(self) -> int:
        return self.minimum
        
