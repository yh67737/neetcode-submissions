class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue=collections.deque()
        heap=[]
        count=[0]*26
        time=0
        for i in tasks:
            count[ord(i)-ord("A")]+=1
        for i in range(26):
            if count[i]!=0:
                heapq.heappush(heap,-count[i])
        while heap or queue:
            if not heap:
                time=queue[0][1]
            while queue and queue[0][1]<=time:
                heapq.heappush(heap,-queue[0][0])
                queue.popleft()
            c=heapq.heappop(heap)
            time+=1
            if c<-1:
                queue.append((-c-1,time+n))
        return time


