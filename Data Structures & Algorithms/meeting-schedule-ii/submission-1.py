"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        ans=0
        endlist=[]
        end=intervals[0].end
        heapq.heappush(endlist,end)
        for i in range(1,len(intervals)):
            c=heapq.heappop(endlist)
            if intervals[i].start>=c:
                heapq.heappush(endlist,intervals[i].end)
            else:
                heapq.heappush(endlist,c)
                heapq.heappush(endlist,intervals[i].end)
        return len(endlist)



        