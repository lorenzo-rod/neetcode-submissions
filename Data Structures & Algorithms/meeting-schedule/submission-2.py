"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda interval : interval.start)
        end = intervals[0].end
        for interval in intervals[1:]:
            start = interval.start
            if start < end:
                return False
            end = interval.end
        return True