class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pos_diag = set()
        neg_diag  = set()
        board = [["."]*n for _ in range(n)]
        res = []

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board].copy())
                return

            for c in range(n):
                if c in col or (r+c) in pos_diag or (r-c) in neg_diag:
                    continue
                
                board[r][c]="Q"
                col.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)
                backtrack(r+1)

                col.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)
                board[r][c]="."

        backtrack(0)
        print(res)
        return res