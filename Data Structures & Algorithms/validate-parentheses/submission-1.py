class Solution:
    def isValid(self, s: str) -> bool:
        #use a stack, and for every opening bracket, push the 
        #corresponding closing bracket onto the stack, now if 
        #we read a closing bracket, it is only valid if it matches
        #the closing bracket on the top of the stack

        # [[(())]]
        # [[((
        
        stack = []
        brackets = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        for c in s:
            if c in ['}', ')', ']']:
                if len(stack) == 0:
                    return False
                top = stack.pop(len(stack)-1)
                if top != brackets[c]:
                    print(top,brackets[c])
                    return False
            else:
                stack.append(c)

        return len(stack) == 0


            


        

        