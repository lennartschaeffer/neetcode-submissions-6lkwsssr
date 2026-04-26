class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
            if openCount < n, then we append an ( and backtrack
            then pop after
            if closedCount < openCount, then we append an ) and backtrack
            then pop after
        """
        res = []
        curr = []
        openCount = 0
        closedCount = 0

        def backtrack(i):   
            nonlocal openCount
            nonlocal closedCount
            
            if i == n * 2:
                currStr = ''.join(curr.copy())
                res.append(currStr)
                return

            if openCount < n:
                curr.append('(')
                openCount += 1
                backtrack(i+1)
                curr.pop()
                openCount -=1
            
            if closedCount < openCount:
                curr.append(')')
                closedCount += 1
                backtrack(i+1)
                curr.pop()
                closedCount -= 1

        backtrack(0)

        return res

        
            
