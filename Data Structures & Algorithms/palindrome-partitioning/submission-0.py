class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        #backtracking function, check

        def backtrack(startIdx):
            if startIdx == len(s):
                res.append(path[:])
                return
            
            for i in range(startIdx, len(s)):
                curr = s[startIdx:i+1]
                if curr == curr[::-1]:
                    path.append(curr)
                    backtrack(i + 1)
                    path.pop()

        backtrack(0)

        return res
