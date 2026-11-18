class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i,c in enumerate(stones):
            stones[i]=-c
        heapq.heapify(stones)
        while len(stones)>=2:
            n1=-heapq.heappop(stones)
            n2=-heapq.heappop(stones)
            if n1!=n2:
                n3=abs(n1-n2)
                heapq.heappush(stones,-n3)
        if stones:
            return -stones[0]
        return 0
