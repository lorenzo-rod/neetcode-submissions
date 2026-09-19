"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        occupances = []

        for interval in intervals:
            occupances.append((interval.start, 1))
            occupances.append((interval.end, -1))
        
        occupances.sort()
        count = 0
        res = 0

        for occupance in occupances:
            count += occupance[1]
            res = max(res, count)
        
        return res
        