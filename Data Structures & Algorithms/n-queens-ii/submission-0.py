class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0

        col = set()
        pos_diag = set()
        neg_diag = set()

        def backtrack(r):
            if r == n:
                nonlocal res
                res+=1
            for c in range(n):
                if c in col or (r+c) in pos_diag or (r-c) in neg_diag:
                    continue

                col.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)

                backtrack(r+1)
                
                col.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)


        backtrack(0)
        return res 