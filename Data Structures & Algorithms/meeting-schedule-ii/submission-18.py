"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [interval.start for interval in intervals]
        ends = [interval.end for interval in intervals]

        starts.sort()
        ends.sort()

        count = 0
        i = 0

        for start in starts:
            if start < ends[i]:
                count += 1
            else:
                i += 1
        
        return count