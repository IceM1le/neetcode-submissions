class Twitter:
    import heapq
    from collections import defaultdict

    def __init__(self):
        self.followers = defaultdict(set)
        self.posts = defaultdict(list)
        self.ident = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.posts[userId], (self.ident, tweetId))
        if len(self.posts[userId]) > 10: heapq.heappop(self.posts[userId])
        self.ident += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for ident, post in self.posts[userId]:
            heapq.heappush(res, (-ident, post))
        for f in self.followers[userId]:
            for ident, post in self.posts[f]:
                heapq.heappush(res, (-ident, post))
        return [heapq.heappop(res)[1] for _ in range(min(len(res), 10))]
                        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
