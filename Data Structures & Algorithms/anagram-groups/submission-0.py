class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        list_strs = []

        for str in strs:
            #create the key as a sorted version of the string
            key = ''.join(sorted(str))
            if key in anagram_map:
                anagram_map[key].append(str)
            else:
                anagram_map[key] = []
                anagram_map[key].append(str)
            
        for s in anagram_map:
            list_strs.append(anagram_map[s])

        return list_strs

