"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # brute force solution would be to compare each meeting
        # to all the other meetings in a double for loop
        # for i in range(len(intervals)):
        #     for j in range(len(intervals)):
        #         if i != j:
        #             if (intervals[i].end > intervals[j].start
        #                 and intervals[i].start < intervals[j].end):
        #                 return False

        intervals.sort(key=lambda i: i.start)

        for i in range(len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
                return False

        return True