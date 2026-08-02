class Twitter:

    def __init__(self):
        self._follows = {}
        self._tweets = {}
        self._count = 0
        # Users => {userID:int :: [followers:List[int]]}
        # Tweets => {userID:int :: List[Tuple[int, int]]}
    
    def _userCheck(self, userId:int) -> None:
        if userId not in self._follows:
            self._follows[userId]=set()
        if userId not in self._tweets:
            self._tweets[userId]=[]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._count+=1
        self._userCheck(userId)
        self._tweets[userId].append((self._count, tweetId))
        print(f"Tweets for user {userId}: {self._tweets[userId]}")   

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        res += self._tweets[userId]
        for followee in self._follows[userId]:
            if followee==userId:
                continue
            for tweet in self._tweets[followee]:
                res.append(tweet)
        if len(res)<=10:
            print(res)
            res.sort(reverse=True)
            return [y for x,y in res]
        else:
            return [y for x,y in heapq.nlargest(10, res)]



    def follow(self, followerId: int, followeeId: int) -> None:
        self._userCheck(followerId)
        self._follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self._follows[followerId].discard(followeeId)
