class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        q = deque()
        step=0
        res = -1
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==2:
                    q.append((i,j,step))

        while q:
            row, col, depth = q.popleft()
            for dx, dy in directions:
                nr, nc = row+dx, col+dy
                if (nr<0 or nc<0 or nr>=ROWS or nc>=COLS
                    or grid[nr][nc]!=1):
                    continue
                grid[nr][nc]=2
                q.append((nr,nc, depth+1))
                step = depth+1

        for row in grid:
            for item in row:
                if item==1:
                    return -1

        return step