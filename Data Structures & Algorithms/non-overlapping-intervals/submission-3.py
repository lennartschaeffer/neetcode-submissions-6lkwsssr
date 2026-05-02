class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
            [1,2],[1,4],[2,4]
        """

        intervals.sort(key=lambda x: [x[1], x[0]])

        res = 0
        prev = intervals[0]

        for i in range(1,len(intervals)):
            start, end = intervals[i]

            if start < prev[1]:
                res += 1
            else:
                prev = intervals[i]
        
        return res
