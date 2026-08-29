class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l,r = 1,0
        res = []
        cur = []

        # valid condition l>=r ==n
        def dfs(l,r):
            if l==r and n==l:
                res.append("".join(cur))
                return
            
            if l<n:
                cur.append("(")
                dfs(l+1, r)
                cur.pop()

            if r<l:
                cur.append(")")
                dfs(l,r+1)
                cur.pop()
                
        dfs(0,0)
        return res