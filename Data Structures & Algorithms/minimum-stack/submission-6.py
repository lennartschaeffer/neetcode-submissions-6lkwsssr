class MinStack:
    """
        prefix approach: keep track of the min element, and any time you add a value
        to the stack you store the min element at the time of adding that value along with
        it. when you pop, make sure to update min element to whatever is the min element
        on the top

    """
    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        #do the append first so that its the previous minElement, not current
        if not len(self.s):
            prevMin = val
        else:
            prevMin = min(self.s[-1][0], self.s[-1][1])

        self.s.append((val, prevMin)) 

    def pop(self) -> None:
        if not len(self.s):
            return
        self.s.pop()

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        val,prevMin = self.s[-1]
        return min(val, prevMin)
        
