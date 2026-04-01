class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        seen = set()
        #loop through array, sort the string and check if the sorted version is in the list 
        for i in range(len(strs)):
            sortedWord = ','.join(sorted(strs[i]))
            if sortedWord not in seen:
                seen.add(sortedWord)
                group = []
                group.append(strs[i])

                for j in range(i+1, len(strs)):
                    if sorted(strs[i]) == sorted(strs[j]) :
                        group.append(strs[j])
                res.append(group)

        return res
