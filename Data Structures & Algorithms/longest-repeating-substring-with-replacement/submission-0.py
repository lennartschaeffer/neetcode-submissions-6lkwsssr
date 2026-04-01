class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #use a hash map to count occurrences
        occ = {}
        l = 0
        maxSize = 0
        for r in range(len(s)):
            occ[s[r]] = occ.get(s[r], 0) + 1 #count occurrence
            size = (r - l) + 1
            #get max frequency
            maxFreq = max(occ.values())
            if size - maxFreq <= k:
                maxSize = max(size, maxSize)
            #while len of string - maxFreq > k, inc. the left 
            #pointer 
            while (size - maxFreq) > k:
                print(occ)
                #decrement the count of that letter
                occ[s[l]] -= 1
                l += 1
                #recalculate the maximum freq and size
                maxFreq = max(occ.values())
                size = (r - l) + 1

        return maxSize
            

