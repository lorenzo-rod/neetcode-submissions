"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        occupances = [0] * (10**6 + 1)

        for interval in intervals:
            start, end = interval.start, interval.end

            for i in range(start, end):
                occupances[i] += 1
            
        return max(occupances)
                    