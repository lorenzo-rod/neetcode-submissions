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
        n = len(intervals)

        for i in range(n):
            max_end = max(max_end, intervals[i].end)
        
        occupances = [0] * (max_end + 1)

        for interval in intervals:
            occupances[interval.start] += 1
            occupances[interval.end] -= 1
        
        res = 0
        count = 0

        for i in range(max_end + 1):
            count += occupances[i]
            res = max(res, count)
        
        return res
