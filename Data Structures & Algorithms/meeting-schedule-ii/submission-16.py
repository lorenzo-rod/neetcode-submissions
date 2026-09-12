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

        for interval in intervals:
            occupances[interval.start] += 1
            occupances[interval.end] -= 1
        
        rooms = 0
        res = 0

        for n in occupances:
            rooms += n
            res = max(res, rooms)
        
        return res
        