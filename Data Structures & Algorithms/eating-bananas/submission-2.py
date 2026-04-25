import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = 0 

        def get_time(rate):
            return sum(math.ceil(p/rate) for p in piles)

        while l<=r:
            mid = (r+l)//2
            if get_time(mid)>h:
                l = mid+1
            else:
                k = mid
                r = mid-1
        return k
            