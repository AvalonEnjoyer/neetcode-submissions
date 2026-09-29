class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        q = deque()
        fresh=0
        time=0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1

        while fresh>0 and q:
            length = len(q)
            for i in range(length):
                row, col = q.popleft()

                for dx, dy in directions:
                    nr, nc = row+dx, col+dy
                    if (nr<0 or nc<0 or nr>=ROWS or nc>=COLS
                        or grid[nr][nc]!=1):
                        continue
                    fresh-=1
                    grid[nr][nc]=2
                    q.append((nr,nc))
            time +=1

        return time if fresh ==0 else -1