class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #left,right pointer to maintain a window, check if each character from t is in window
        minSub = s

        for i in range(len(s)):
            for j in range(i, len(s)):
                containsString = True
                subString = s[i:j+1]
                lettersSeen = list(s[i:j+1])
                for c in t:
                    if c not in lettersSeen:
                        containsString = False
                    else:
                        lettersSeen.remove(c)
                if containsString:
                    print(subString, minSub)
                    if len(subString) < len(minSub):
                        minSub = subString

        sList = list(s)
        containsString = True
        for c in t:
            if c not in sList:
                containsString = False
            else:
                sList.remove(c)
        
        if not containsString:
            return ""
        
        return minSub
