class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        one, two = 1, 0
        for i in range(n-1,-1,-1):
            if s[i]=="0":
                two, one = one, 0
            else:
                res=one
                if i<n-1 and 9<int(s[i:i+2])<27:
                    res+=two
                two, one = one, res

        return one
