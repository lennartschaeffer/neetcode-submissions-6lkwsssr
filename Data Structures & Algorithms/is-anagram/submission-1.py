class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create two hashmaps where 
        #key = letter,
        #value = number of occurences
        #first compare to see if the keys are the same
        #if they are, compare if values are the same
        #if they are, return true

        s_map = {}
        t_map = {}

        for i in range(len(s)):
            s_map[s[i]] = s_map.get(s[i], 0) + 1

        for i in range(len(t)):
            t_map[t[i]] = t_map.get(t[i], 0) + 1
        
        if s_map.keys() == t_map.keys():
            for key in s_map:
                if s_map[key] == t_map[key]:
                    return True
               
                
        return False