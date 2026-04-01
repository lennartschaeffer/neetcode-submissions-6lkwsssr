class Solution:
    def minWindow(self, s: str, t: str) -> str:

        countT,window = {},{}
        for c in t:
            countT[c] = countT.get(c,0) + 1
        
        res = (-1,-1)
        resLen = float("inf")
        l = 0
        have,need = 0,len(countT)

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0) + 1
            
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                size = (r - l + 1) #check size and compare to res
                if size < resLen:
                    print(s[l:r+1])
                    res,resLen = (l,r),size
                #move left up, check if that affected the window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        
        if resLen == float("inf"):
            return ""
        
        
        return s[res[0]:res[1]+1]

                    

