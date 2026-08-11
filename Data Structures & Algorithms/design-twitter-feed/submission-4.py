from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.tweets = defaultdict(list)
        self.count = 0    

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.users[userId].add(userId)
        data = []

        for followee in self.users[userId]:
            if self.tweets[followee]:
                index = len(self.tweets[followee]) - 1
                count, tweetId = self.tweets[followee][index]
                data.append((count, tweetId, followee, index - 1))
        heapq.heapify(data)

        res = []

        while data and len(res) < 10:
            count, tweetId, followee, index = heapq.heappop(data)
            res.append(tweetId)
            if index > -1:
                heapq.heappush(data, (self.tweets[followee][index][0], self.tweets[followee][index][1], followee, index - 1))
        
        return res
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.users[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.users[followerId].discard(followeeId)
