from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [[0,-1],[0,1],[-1,0],[1,0]]

        def bfs(row,col):
            q = deque()
            q.append((row,col))
            grid[row][col]="0"
            
            while q:
                r,c = q.popleft()
                for dx, dy in directions:
                    nr, nc = r+dx, c+dy
                    if (nr < 0 or nc < 0 or nr >= m or nc >= n or grid[nr][nc]=="0"):
                        continue
                    grid[nr][nc] = "0"
                    q.append((nr,nc))

        ans = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col]=="1":
                    bfs(row, col)
                    ans+=1
        return ans