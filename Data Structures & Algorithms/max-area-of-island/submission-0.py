from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = [0]
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c]=0
            ans = 1
            
            while q:
                row, col = q.popleft()
                for x,y in directions:
                    nr, nc = row+x, col+y
                    if (nr<0 or nc<0 or nr>=ROWS or nc>=COLS or grid[nr][nc]==0):
                        continue
                    ans += 1
                    q.append((nr,nc))
                    grid[nr][nc]=0
            res.append(ans)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    bfs(i,j)
        return max(res)