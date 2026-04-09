class Solution:
    def checkValidString(self, s: str) -> bool:
        opening = []
        stars = []
        for i in range(len(s)):
            if s[i] == '(':
                opening.append(i)
            elif s[i] == '*':
                stars.append(i)
            else:
                if len(opening):
                    opening.pop()
                elif len(stars):
                    stars.pop()
                else:
                    return False
        
        while len(opening):
            if not len(stars):
                return False
            o = opening.pop()
            st = stars.pop()
            if o > st:
                return False
        
        return True

