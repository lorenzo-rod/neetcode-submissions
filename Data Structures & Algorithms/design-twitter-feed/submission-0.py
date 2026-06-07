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
        min_heap = []
        res = []
        for followeeId in self.users[userId]:
            if self.tweets[followeeId]:
                index = len(self.tweets[followeeId]) - 1
                count, tweetId = self.tweets[followeeId][index]
                min_heap.append((count, tweetId, followeeId, index - 1))
        heapq.heapify(min_heap)
        while min_heap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(min_heap)
            res.append(tweetId)
            if index > -1:
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(min_heap, (count, tweetId, followeeId, index - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.users[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
