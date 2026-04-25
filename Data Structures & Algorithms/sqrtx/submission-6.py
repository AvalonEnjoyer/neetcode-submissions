class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        res = 0 
        while l<=r:
            mid=(r+l)//2
            if x//mid>mid:
                l = mid + 1
            elif x//mid<mid:
                r = mid - 1
            else:
                return mid
        return r       