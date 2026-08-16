import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.tweets = defaultdict(list)
        self.count = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop(0)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.users[userId].add(userId)
        data = []
        for followeeId in self.users[userId]:
            index = len(self.tweets[followeeId]) - 1
            if index > -1:
                count, tweetId = self.tweets[followeeId][index]
                data.append((count, tweetId, index, followeeId))
        heapq.heapify(data)

        res = []

        while data and len(res) < 10:
            _, tweetId, index, followeeId = heapq.heappop(data)
            res.append(tweetId)
            if index > 0:
                count, tweetId = self.tweets[followeeId][index - 1]
                heapq.heappush(data, (count, tweetId, index - 1, followeeId))
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.users[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.users[followerId].discard(followeeId)
        
