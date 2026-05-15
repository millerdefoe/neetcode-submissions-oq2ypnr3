class Twitter:

    def __init__(self):
        self.follow_table = defaultdict(set)
        self.user_to_tweet = defaultdict(list)
        self.timer = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_to_tweet[userId].append((self.timer, tweetId))
        self.timer += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        
        # Include the user themselves
        all_users = self.follow_table[userId] | {userId}
        
        for user in all_users:
            tweets = self.user_to_tweet[user]
            if tweets:
                # Start from the most recent tweet of each user
                idx = len(tweets) - 1
                timestamp, tweetId = tweets[idx]
                heapq.heappush(min_heap, (-timestamp, tweetId, user, idx))
        
        res = []
        while min_heap and len(res) < 10:
            timestamp, tweetId, user, idx = heapq.heappop(min_heap)
            res.append(tweetId)
            if idx > 0:
                # Push that user's next most recent tweet
                idx -= 1
                timestamp, tweetId = self.user_to_tweet[user][idx]
                heapq.heappush(min_heap, (-timestamp, tweetId, user, idx))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_table[followerId].add(followeeId)
        self.follow_table[followerId].add(followerId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_table[followerId]:
            self.follow_table[followerId].remove(followeeId)
