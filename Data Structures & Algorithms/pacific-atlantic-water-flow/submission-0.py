class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        pac = set()
        atl = set()

        def dfs(r,c,visit,prev):
            if ((r,c) in visit or
                r<0 or c<0 or r==ROWS
                or c==COLS or heights[r][c]<prev):
                return
            visit.add((r,c))
            for dr, dc in directions:
                dfs(r+dr, c+dc, visit, heights[r][c])
        
        for i in range(ROWS):
            dfs(i,0, pac, heights[i][0])
            dfs(i,COLS-1,atl,heights[i][COLS-1])
        
        for j in range(COLS):
            dfs(0,j,pac,heights[0][j])
            dfs(ROWS-1,j, atl, heights[ROWS-1][j])

        res = []

        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in pac and (i,j) in atl:
                    res.append((i,j))
        
        return res