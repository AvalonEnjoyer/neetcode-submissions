class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [[] for _ in range(n+1)]
        res[0] = [""]

        for k in range(1,n+1):
            for i in range(k):
                for left in res[i]:
                    for right in res[k-i-1]:
                        res[k].append("("+left+")"+right)
        print(res)
        return res[-1]