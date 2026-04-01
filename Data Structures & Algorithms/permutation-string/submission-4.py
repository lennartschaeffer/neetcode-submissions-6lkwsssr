class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        #get the characters in s1
        count1 = {}
        for c in s1:
            count1[c] = count1.get(c, 0) + 1
        #use the length of s1 for the window in s2
        window = len(count1)

        for i in range(len(s2)):
            count2 = {}
            curr = 0
            for j in range(i, len(s2)):
                count2[s2[j]] = count2.get(s2[j],0) + 1
                if count2[s2[j]] > count1.get(s2[j], 0):
                    break
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    curr += 1
                if curr == window:
                    return True

        return False



