class MedianFinder:

    def __init__(self):
        self.left=[]
        self.right=[]
        

    def addNum(self, num: int) -> None:
        if not self.left or not self.right:
            heapq.heappush(self.left,-num)
        else:
            if num<=-self.left[0]:
                heapq.heappush(self.left,-num)
            else:
                heapq.heappush(self.right,num)
        while abs(len(self.left)-len(self.right))>1:
            if len(self.left)>len(self.right):
                left=-heapq.heappop(self.left)
                heapq.heappush(self.right,left)
            else:
                right=heapq.heappop(self.right)
                heapq.heappush(self.left,-right)


        

    def findMedian(self) -> float:
        if len(self.right)==len(self.left):
            left=-self.left[0]
            right=self.right[0]
            return (left+right)/2
        if len(self.right)>len(self.left):
            return self.right[0]
        if len(self.right)<len(self.left):
            return -self.left[0]