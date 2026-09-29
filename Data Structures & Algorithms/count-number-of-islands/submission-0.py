class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        m = len(grid)
        n = len(grid[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= m or c >= n or
                    (r, c) in visited or grid[r][c] == "0"):
                return 0
            visited.add((r, c))
            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            grid[r][c] = "1"
            return 1

        ans = 0
        for r in range(m):
            for c in range(n):
                ans += dfs(r, c)
        return ans