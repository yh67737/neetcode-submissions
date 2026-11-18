from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for i in points:
            x=i[0]
            y=i[1]
            dis=sqrt(x**2+y**2)
            heapq.heappush(heap,(-dis,i))
            if len(heap)>k:
                heapq.heappop(heap)
        ans=[]
        if heap:
            for i in heap:
                ans.append(i[1])
        return ans
        

        