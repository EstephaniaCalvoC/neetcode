class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = float('inf')
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0) # [0]
            self.min_value = val # 1
        else:
            self.stack.append(val - self.min_value) # [0, 1], [0, 1, -1], [0, 1, -1, 2]
            self.min_value = min(val, self.min_value) # 1, 0, 0
        
    def pop(self) -> None:
        removed = self.stack[-1]
        if removed < 0:
            self.min_value = self.min_value - removed
        self.stack = self.stack[0: -1]

    def top(self) -> int:
        top_diff = self.stack[-1]
        if top_diff > 0:
            return top_diff + self.min_value
        else:
            return self.min_value

    def getMin(self) -> int:
        return self.min_value


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(1)
    minStack.push(2)
    minStack.push(0)
    print(minStack.getMin()) # return 0
    minStack.pop()
    print(minStack.top()) # return 2
    print(minStack.getMin()) # return 1