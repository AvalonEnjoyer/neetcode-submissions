class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        squares  = defaultdict(set)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                cur = board[i][j]
                if board[i][j]==".":
                    continue
                if cur in row[i] or cur in col[j] or cur in squares[(i//3,j//3)]:
                    return False
                row[i].add(cur)
                col[j].add(cur)
                squares[(i//3,j//3)].add(cur)
        
        return True