class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])

        def dfs(x,y, found):
            if found == len(word):
                return True
            if min(x,y)<0 or x>= rows or y>=columns or board[x][y] == "#" or board[x][y] != word[found]:
                return False
            else:
                temp, board[x][y] = board[x][y], "#"
                down = dfs(x+1,y, found+1)
                up = dfs(x-1,y, found+1)
                right = dfs(x,y+1, found+1)
                left = dfs(x,y-1, found+1)
                res = left or right or up or down
                board[x][y]=temp
                return res

        for i in range(rows):
            for j in range(columns):
                if dfs(i,j,0):
                    return True
        
        return False