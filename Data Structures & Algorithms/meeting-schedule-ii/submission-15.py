"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([interval.start for interval in intervals])
        ends = sorted([interval.end for interval in intervals])

        end_p = 0
        res = 0

        for start in starts:
            if start < ends[end_p]:
                res += 1
            else:
                end_p += 1
        
        return res
