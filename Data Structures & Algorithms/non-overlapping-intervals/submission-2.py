class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort the intervals array
        # if curr[end] > curr+1[start] this means they overlap, so we increment by one
        intervals.sort()
        # [[1,2],[1,3],[2,3],[3,4]]
        # 2 => 2 => 3 => 3
        currEnd = intervals[0][1]
        count = 0
        for i in range(1,len(intervals)):
            start, end = intervals[i]
            if start >= currEnd:
                currEnd = end
            else:
                count += 1
                currEnd = min(currEnd,end)
        
        return count
