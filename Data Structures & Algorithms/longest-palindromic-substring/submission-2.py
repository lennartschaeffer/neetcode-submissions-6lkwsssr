class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        res = 0

        # abbc
        # abbbbc
        # naan

        for i in range(len(s)):
            l,r = i,i
            if resLen == 0:
                resLen = 1
                res = i
            while l > 0 and r < len(s)-1: #check odd length palindromes
                l -= 1
                r += 1
                if s[l] == s[r]:
                    currLen = (r - l) + 1
                    if currLen > resLen:
                        resLen = currLen
                        res = l
                else:
                    break
            
            if i < len(s)-1 and s[i] == s[i+1]:
                l,r = i, i+1
                currLen = 2
                if currLen > resLen:
                    resLen = currLen
                    res = l
                while l > 0 and r < len(s)-1:
                    l -= 1
                    r += 1
                    if s[l] == s[r]:
                        currLen = (r - l) + 1
                        if currLen > resLen:
                            resLen = currLen
                            res = l
                    else:
                        break

        print(res,resLen)

        return s[res:res+resLen]

