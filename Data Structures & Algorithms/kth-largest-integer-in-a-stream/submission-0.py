class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.n=nums
        self.k=k
        heapq.heapify(self.n)
        while len(self.n)>self.k:
            heapq.heappop(self.n)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.n,val)
        while len(self.n)>self.k:
            heapq.heappop(self.n)
        return self.n[0]
        
