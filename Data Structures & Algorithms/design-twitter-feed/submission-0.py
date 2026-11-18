class Twitter:

    def __init__(self):
        self.followmap={}
        self.tweetmap={}
        self.count=0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count+=1
        if userId in self.tweetmap:
            self.tweetmap[userId].append((self.count,tweetId))
        else:
            self.tweetmap[userId]=[(self.count,tweetId)]
        return

        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap=[]
        ans=[]
        if userId in self.tweetmap:
            for i in self.tweetmap[userId]:
                heapq.heappush(heap,i)
                while len(heap)>10:
                    heapq.heappop(heap)

        if userId in self.followmap:
            for i in self.followmap[userId]:
                if i in self.tweetmap:
                    for j in self.tweetmap[i]:
                        heapq.heappush(heap,j)
                        while len(heap)>10:
                            heapq.heappop(heap)
        if heap:
            heap.sort()
            for i in heap:
                ans.append(i[1])
        return ans[::-1]


        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId==followeeId:
            return
        if followerId in self.followmap:
            if followeeId in self.followmap[followerId]:
                return
            self.followmap[followerId].append(followeeId)
        else:
            self.followmap[followerId]=[followeeId]
        return 
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followmap:
            return
        if followeeId not in self.followmap[followerId]:
            return
        self.followmap[followerId].remove(followeeId)
        return
        
