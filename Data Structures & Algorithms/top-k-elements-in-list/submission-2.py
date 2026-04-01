class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # loop through list, map each number to amount of occurrences
        # then get the map.values(), sort it and return the k max elements
        res = {}

        for n in nums:
            res[n] = res.get(n, 0) + 1

        vals = res.values()

        topK = sorted(vals)[len(vals)-k:len(vals)]

        topNums = []

        for n in res.keys():
            if res[n] in topK:
                topNums.append(n)
        
        
        return topNums
