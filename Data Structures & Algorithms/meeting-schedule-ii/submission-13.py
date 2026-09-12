"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        max_end = 0

        for interval in intervals:
            max_end = max(max_end, interval.end)
        
        occupances = [0] * (max_end + 1)
        res = 0

        for interval in intervals:
            start, end = interval.start, interval.end

            for i in range(start, end):
                occupances[i] += 1
                res = max(res, occupances[i])
        
        return res