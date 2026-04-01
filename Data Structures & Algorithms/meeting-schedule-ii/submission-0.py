"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        arr = []

        for ivl in intervals:
            arr.append((ivl.start,1))
            arr.append((ivl.end,-1))
        
        arr.sort()

        currDays = 0
        minDays = 0

        for time, startOrEnd in arr:
            currDays += startOrEnd
            minDays = max(minDays,currDays)
        
        return minDays