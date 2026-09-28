class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pos_diag = set()
        neg_diag  = set()
        board = [["."]*n for _ in range(n)]
        res = []

        # def valid(board, row, col):
        #     # checking the same row
        #     if "Q" in board[row]:
        #         return False
        #     # checking the left diagonal
        #     i,j = row-1, col-1
        #     while i>=0 and j>=0:
        #         if board[i][j]=="Q":
        #             return False
        #         i-=1
        #         j-=1
        #     # checking the bottom left diagonal
        #     i,j = row+1, col-1
        #     while i<n and j<n:
        #         if board[i][j]=="Q":
        #             return False
        #         i+=1
        #         j-=1
        #     return True

        def backtrack(r):
            if r == n:
                temp = ["".join(row) for row in board]
                res.append(temp)
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
        return res