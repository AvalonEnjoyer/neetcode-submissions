class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[-1,0],[1,0],[0,1],[0,-1]]

        q = deque()
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]==0:
                    q.append((row,col))

        while q:
            row, col= q.popleft()
            for dx, dy in directions:
                nr, nc = row+dx, col+dy
                if (nr<0 or nc<0 or nr>=ROWS or nc>=COLS
                    or grid[nr][nc]!=inf):
                    continue

                grid[nr][nc]=grid[row][col]+1
                q.append((nr,nc))
