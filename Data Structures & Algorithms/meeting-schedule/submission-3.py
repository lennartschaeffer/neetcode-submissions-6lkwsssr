"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
            is the question just asking for any meetings that overlap?
            [(0,30),(5,10),(15,20)]
            [(5,10),(15,20),(0,30) ]
            [(0,4), (5,10)]
            if the current interval starts before the previous one ends
            if the current interval ends after the next one starts
        """
        intervals.sort(key=lambda x: x.end)
        for i in range(len(intervals)):
            if i > 0:
                prevStart, prevEnd = intervals[i-1].start,intervals[i-1].end
                start, end = intervals[i].start, intervals[i].end
                if start < prevEnd:
                    return False
        
        return True
