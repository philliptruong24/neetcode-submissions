class Twitter:

    def __init__(self):
        self.hashtable = {}
        self.recency = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.hashtable:
            self.hashtable[userId] = ([], [])

        self.hashtable[userId][1].append((self.recency, tweetId))
        self.recency += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        if userId not in self.hashtable:
            return []

        arr = [userId]
        for followingId in self.hashtable[userId][0]:
            arr.append(followingId)

        for personId in arr:
            for recency, tweetId in self.hashtable[personId][1]:
                heapq.heappush(minHeap, (-recency, tweetId))
        
        res = []
        for i in range(10):
            if minHeap:
                recency, tweetId = heapq.heappop(minHeap)
                res.append(tweetId)
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.hashtable:
            self.hashtable[followerId] = ([], [])
        
        if followeeId not in self.hashtable[followerId][0]:    
            self.hashtable[followerId][0].append(followeeId)
        


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.hashtable and followeeId in self.hashtable[followerId][0]:

            self.hashtable[followerId][0].remove(followeeId)
        
