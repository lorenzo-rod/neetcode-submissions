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
        i = 0
        j = 0
        count = 0
        max_count = 0
        while i < len(intervals) and j < len(intervals):
            if starts[i] < ends[j]:
                i += 1
                count += 1
                max_count = max(max_count, count)
            else:
                j += 1
                count -= 1
        return max_count
        