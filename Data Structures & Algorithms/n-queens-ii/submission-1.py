class Solution:
    def totalNQueens(self, n: int) -> int:
        col = 0
        pos_diag = 0
        neg_diag = 0
        res = 0

        def backtrack(r):
            nonlocal col, pos_diag, neg_diag, res
            if r == n:
                res+=1
                return 
            
            for c in range(n):
                if (col&(1<<c)) or (pos_diag&(1<<(r+c))) or (neg_diag&(1<<(r-c+n))):
                    continue
                
                col ^= (1<<c)
                pos_diag ^= (1<<(r+c))
                neg_diag ^= (1<<(r-c+n))

                backtrack(r+1)
                
                col ^= (1<<c)
                pos_diag ^= (1<<(r+c))
                neg_diag ^= (1<<(r-c+n))

        backtrack(0)
        return res 