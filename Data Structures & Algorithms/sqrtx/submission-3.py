class Solution:
    def mySqrt(self, x: int) -> int:
        # sqrt_dict={
        #     0:0,
        #     1:1}
        # if x ==0 or x==1:
        #     return sqrt_dict[x]
        # if x ==0:
        #     return 0
        l = 1
        r = x 
        while l<=r:
            mid=(r+l)//2
            sqr = mid*mid
            if sqr==x:
                return mid
            elif sqr>x:
                r = mid - 1
            else:
                l = mid + 1
        return r            