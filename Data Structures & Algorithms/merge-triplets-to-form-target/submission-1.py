class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        if we can iterate through the triplets and check
        that for each position in the target, those values
        exist, then there must be some way to apply the operations
        we know that we can skip any triplets with a value greater 
        than whats in target
        """ 
        res = [False] * 3
        for trip in triplets:
            a,b,c = trip
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            if a == target[0]:
                res[0] = True
            if b == target[1]:
                res[1] = True
            if c == target[2]:
                res[2] = True
        
        for r in res:
            if not r:
                return False
        
        return True