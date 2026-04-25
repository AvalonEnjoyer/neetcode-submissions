import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = 0 

        def get_time(rate):
            res = 0
            i = 0
            while res <= h and i<len(piles):
                res += math.ceil(piles[i]/rate)
                i+=1
            return res

        while l<=r:
            mid = (r+l)//2
            print(f"{get_time(mid)} hours when rate is {mid}")
            if get_time(mid)>h:
                l = mid+1
            else:
                k = mid
                r = mid-1
        return k
            