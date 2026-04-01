class Solution:
    def countSubstrings(self, s: str) -> int:
        # use the same even and odd counting strategy as in the previous one

        count = 0
        for i in range(len(s)):
            count += 1
            l,r = i-1,i+1
            while l >= 0 and r < len(s): # check odd length palindromes
                if s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
                else:
                    break
            if i < len(s)-1 and s[i] == s[i+1]: # even lengths
                count += 1
                l = i - 1
                r = i + 2
                print(i,s[i:i+2])
                while l >= 0 and r < len(s):
                    if s[l] == s[r]:
                        count += 1
                        l -= 1
                        r += 1
                    else:
                        break
            
        return count
