class Twitter:

    def __init__(self):
        self._follows = {}
        self._tweets = {}
        self._count = 0
        # Users => {userID:int :: [followers:List[int]]}
        # Tweets => {userID:int :: List[Tuple[int, int]]}
    
    def _userCheck(self, userId:int) -> None:
        if userId not in self._follows:
            self._follows[userId]={userId}
        if userId not in self._tweets:
            self._tweets[userId]=deque([])

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._count+=1
        self._userCheck(userId)
        self._tweets[userId].appendleft((self._count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        print(self._tweets)
        res = []
        heapq.heapify(res)
        # Take 0th tweet from the user and each of their followers

        for i in range(10):
            glob_idx = i
            for followee in self._follows[userId]:
                if glob_idx < len(self._tweets[followee]):
                    heapq.heappush(res, self._tweets[followee][glob_idx])
                if len(res)>10:
                    heapq.heappop(res)
            
        f_res = []
        for _ in range(len(res)):
            f_res.append(heapq.heappop(res)[1])
        return f_res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self._userCheck(followerId)
        self._follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self._follows[followerId].discard(followeeId)