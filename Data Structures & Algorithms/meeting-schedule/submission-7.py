"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = [[interval.start, interval.end] for interval in intervals]
        intervals.sort()
        prev_end = -1

        for start, end in intervals:
            if prev_end <= start:
                prev_end = end
            else:
                return False
        
        return True