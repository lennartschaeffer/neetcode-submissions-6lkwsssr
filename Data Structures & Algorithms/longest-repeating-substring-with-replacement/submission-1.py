class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #use a hash map to count occurrences
        occ = {}
        l = 0
        maxSize = 0
        maxFreq = 0

        for r in range(len(s)):
            occ[s[r]] = occ.get(s[r], 0) + 1 #count occurrence
            #get max frequency
            maxFreq = max(maxFreq,occ[s[r]])
            
            #while len of string - maxFreq > k, inc. the left 
            #pointer 
            while ((r - l) + 1 - maxFreq) > k:
                # print(occ)
                print(l)
                #decrement the count of that letter
                occ[s[l]] -= 1
                l += 1
                
            maxSize = max(maxSize, (r - l) + 1)
        return maxSize
            

