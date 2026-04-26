class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        create the mapping of digits to chars
        for each digit j:
            for each character in digitMapping[j]:
                append(j)
                recurse(j+1)
                pop()
        """
        curr = []
        res = []
        mapping = {
            '2': 'ABC',
            '3': 'DEF',
            '4': 'GHI',
            '5': 'JKL',
            '6': 'MNO',
            '7': 'PQRS',
            '8': 'TUV',
            '9': 'WXYZ'
        }

        def backtrack(i):
            if curr and len(curr) == len(digits):
                res.append(''.join(curr.copy()))
                return

            for j in range(i,len(digits)):
                chars = mapping[digits[j]]
                for c in chars:
                    curr.append(c.lower())
                    backtrack(j+1)
                    curr.pop()
        
        backtrack(0)

        return res