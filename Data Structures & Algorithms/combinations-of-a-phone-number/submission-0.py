class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterToNums = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"],
        }
        res = []
        def backtrack(i, currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                return
            
            for c in letterToNums[digits[i]]:
                backtrack(i + 1, currStr + c)

        backtrack(0,"")

        return res if len(digits) else []
        

