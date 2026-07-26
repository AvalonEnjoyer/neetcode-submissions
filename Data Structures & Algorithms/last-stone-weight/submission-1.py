class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        print(stones)

        while len(stones) > 1:
            one,two = heapq.heappop(stones), heapq.heappop(stones)
            if one!=two:
                diff = one-two if (one-two)<0 else two-one
                heapq.heappush(stones, diff)

        return 0 if not stones else (-1*heapq.heappop(stones))
