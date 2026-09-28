"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        h = []
        intervals.sort(key=lambda x: (x.start))
        res = 0
        for i in range(len(intervals)):
            while h and h[0] <= intervals[i].start:
                heapq.heappop(h)
            heapq.heappush(h, intervals[i].end)
            res = max(res, len(h))
        return res