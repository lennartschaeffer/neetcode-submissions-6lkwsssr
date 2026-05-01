class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
            sort the intervals by end time
            keep track of latestInterval
            if currInterval overlaps with latest, merge
            if not, append
        """

        res = []
        intervals.sort()

        for start,end in intervals:
            if not len(res) or start > res[-1][1]:
                res.append([start,end])
            else:
                res[-1][0] = min(res[-1][0], start)
                res[-1][1] = max(res[-1][1], end)
        
        return res