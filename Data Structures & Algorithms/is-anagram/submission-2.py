class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #use two hashmaps for each string
        #compare if the hashmaps are equal

        sMap = {}
        tMap = {}

        for l in s:
            sMap[l] = sMap.get(l, 0) + 1
        
        for l in t:
            tMap[l] = tMap.get(l, 0) + 1

        return sMap == tMap