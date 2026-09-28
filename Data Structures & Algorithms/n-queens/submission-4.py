class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        tile = "."
        res = []

        def valid(board, row, col):
            # checking the same row
            if "Q" in board[row]:
                return False
            # checking the left diagonal
            i,j = row-1, col-1
            while i>=0 and j>=0:
                if board[i][j]=="Q":
                    return False
                i-=1
                j-=1
            # checking the bottom left diagonal
            i,j = row+1, col-1
            while i<n and j<n:
                if board[i][j]=="Q":
                    return False
                i+=1
                j-=1
            return True

        def backtrack(board, col):
            if col == n:
                temp = ["".join(board[i]) for i in range(n)]
                res.append(temp.copy())
                return
            for row in range(n):
                if valid(board,row,col):
                    board[row][col]="Q"
                    backtrack(board, col+1)
                    board[row][col]="."

        backtrack([[tile]*n for _ in range(n)],0)
        return res