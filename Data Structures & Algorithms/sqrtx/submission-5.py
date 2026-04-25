class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        res = 0 
        while l<=r:
            mid=(r+l)//2
            sqr = mid*mid
            if sqr>x:
                r = mid - 1
            elif sqr<x:
                l = mid + 1
                res = mid
            else:
                return mid
        return res            