class Twitter:

    def __init__(self):
        self.timer = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.timer, tweetId))
        self.timer -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
    
        users = [userId] + list(self.followMap[userId])

        for user in users:
            if self.tweetMap[user]:
                index = len(self.tweetMap[user]) - 1
                time, tweetId = self.tweetMap[user][index]
                minHeap.append((time, tweetId, user, index))
        
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            time, tweetId, user, index = heapq.heappop(minHeap)

            res.append(tweetId)
            index -= 1
            if index >= 0:
                time, tweetId = self.tweetMap[user][index]
                heapq.heappush(minHeap,(time, tweetId, user, index))

        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
