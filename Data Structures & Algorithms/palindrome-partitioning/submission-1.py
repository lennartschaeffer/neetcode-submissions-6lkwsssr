class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        append,recurse,pop
        at each step, append s[i:j+1]
        recurse on j+i
        pop
        a -> aa -> aab -> POP
        """

        res = []
        curr = []

        def backtrack(i):
            if i == len(s):
                res.append(curr.copy())
                return

            for j in range(i,len(s)):
                st = s[i : j + 1]
                curr.append(st)
                if st == st[::-1]:
                    backtrack(j + 1)
                curr.pop()

        backtrack(0)
        return res
