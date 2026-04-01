class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #keep a stack of the numbers
        #when a mathematical operand is read, based on the operand pop from the number
        #stack and perform the calculation
        stack = []
        #when you perform the calculation, push that back onto the top of the stack
        
        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '-':
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num2 - num1)
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == '/':
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int(float(num2) / num1))
            else:
                stack.append(int(t))
        
        return stack[0]