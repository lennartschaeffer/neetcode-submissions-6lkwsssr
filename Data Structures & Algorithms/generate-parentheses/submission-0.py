class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #use a stack to keep track of the current string of parenthesis
        stack = []
        #results array to append the strings
        res = []

        def backtrack(openAmount, closedAmount):
            #if the amounts are equal, i.e. open == closed == n, then return the string
            if openAmount == closedAmount == n:
                res.append(''.join(stack))
                return
            
            if openAmount < n and closedAmount < n:
                stack.append('(')
                backtrack(openAmount + 1, closedAmount)
                stack.pop()

            if closedAmount < openAmount:
                stack.append(')')
                backtrack(openAmount, closedAmount + 1)
                stack.pop()

        backtrack(0,0)

        return res
        
