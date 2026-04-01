class MinStack:

    def __init__(self):
        self.stack = []
        #for the min elemnt, we can just use a second list that will always
        #have the minimum element on the top
        #1, 
        #1
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        #when pushing to the min stack, push the min
        if len(self.minStack) == 0:
            self.minStack.append(val)
        else:
            self.minStack.append(min(self.minStack[len(self.minStack)-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1] if len(self.stack) > 0 else -1

    def getMin(self) -> int:
        return self.minStack[len(self.minStack)-1]
