class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[-1,0],[1,0],[0,1],[0,-1]]

        def bfs(r,c):
            q = deque()
            q.append((r,c,1))
            
            while q:
                row, col,depth = q.popleft()
                for dx, dy in directions:
                    nr, nc = row+dx, col+dy
                    if (nr<0 or nc<0 or nr>=ROWS or nc>=COLS
                        or grid[nr][nc]==-1 or grid[nr][nc]==0 or grid[nr][nc]<=depth):
                        continue
                    grid[nr][nc]=depth
                    q.append((nr,nc, depth+1))
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]==0:
                    bfs(row,col)
